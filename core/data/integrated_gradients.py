from captum.attr import IntegratedGradients
import core.utils as utils
class IG:
    def __init__(self, model):
        self.model = model
        self.ig = IntegratedGradients(model.model)
      
    def get_ig(self, image):
        image = self.model.transform(image)
        image.requires_grad = True
        model = self.model.model
        # model.eval()
        # model.zero_grad()
        attribution = self.ig.attribute(image, target=self.model.predict_max(image).item() ,return_convergence_delta=False)
        img_data  = attribution
        self.ig_image = utils.tensor2imgTensor(img_data.detach().numpy())
        return attribution
    
    def get_ig_img(self):
        return self.ig_image
