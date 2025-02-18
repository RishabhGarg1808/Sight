from PIL import Image
import torch ,cv2
import numpy as np
import matplotlib.pyplot as plt
from  captum.attr  import  ( 
    LayerAttribution , 
    LayerGradCam , 
    MultiscaleFastCam 
)

def visualize_cam(mask, img):
    heatmap = cv2.applyColorMap(np.uint8(255 * mask), cv2.COLORMAP_JET)
    heatmap = np.float32(heatmap) / 255
    heatmap = heatmap[..., ::-1]  # Convert BGR to RGB
    result = heatmap * 0.4 + np.float32(img)
    result = result / np.max(result)
    return heatmap, result

class GradCAM:
    def __init__(self, model, image,target_layer = None):
        self.model = model
        self.image = image
        self.target_layer = self.model.model.layer4 if target_layer is None else target_layer

    def  normalize (self, x ): 
        _min, _max = x.min(),x.max() 
        return(x - _min ).div(_max - _min ) 

    def fast_cam(self):
        model = self.model.model
        fastcam = MultiscaleFastCam ( model , 
                        layers = [ model . relu , 
                                model.layer1[ 2 ].relu , 
                                model.layer2[ 3 ].relu , 
                                model.layer3[ 5 ].relu , 
                                model.layer4[ 2 ].relu ],
                        ) 
        attributes = fastcam.attribute(self.image, combine = True) 
        csmap = attributes[0].cpu().numpy().transpose(1,2,0).squeeze ()
        return csmap

    def grad_cam(self):
        model = self.model.model
        gradcam = LayerGradCam(model, self.target_layer)
        attribute_gradcam   = gradcam.attribute(self.image ,
                                        target=self.model.predict_max(self.image).item(),
                                        relu_attributions=True)
        attribute_gradcam,  =  LayerAttribution.interpolate (attribute_gradcam ,  
                                                 ( 224 ,224), 
                                                 'bilinear' )
        attribute_gradcam  =  self.normalize(attribute_gradcam ) 
        attribute_gradcam  =  attribute_gradcam.detach().squeeze().cpu().numpy () 
        return attribute_gradcam 
    
    def get_fastcam(self):
        return self.fast_cam()
    
    def get_gradcam(self):
        csmap = self.fast_cam()
        attribute_gradcam = self.grad_cam()
        inclass_map  =  csmap  *  attribute_gradcam 
        outclass_map  =  csmap  *  ( 1  -  attribute_gradcam ) 

        heatmap ,result = visualize_cam(torch.tensor(inclass_map), 
                            self.image.squeeze(0).permute(1,2,0).numpy())
        return result , heatmap
