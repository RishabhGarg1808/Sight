from core.data.gradcam import GradCAM
from core.data.guided_backprop import GuidedBackpropExplainer
from core.data.integrated_gradients import IG
from core.data.saliency import SaliencyAttribution
from PIL import Image
import numpy as np
from PySide6.QtGui import QPixmap ,QImage
from PySide6.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QMainWindow
from PySide6.QtCore import Qt ,Signal

class View(QMainWindow):

    data_generated = Signal()
    def __init__(self,model,image,ui):
        super().__init__()
        self.model = model
        self.image = self.model.transform(image)
        self.ui = ui
        self.transformed_image = self.model.transform(self.image)
    
    #We first call the data_gen to coumpute all data and then we call the viewer to display the data
    def data_gen(self,image= None):
        if image:
            self.transformed_image = self.model.transform(image)
        #gradcam data_gen
        gradcam = GradCAM(self.model, self.transformed_image)
        heatmap , result_image = gradcam.get_gradcam()
        pil_image = Image.fromarray((result_image * 255).astype(np.uint8))
        pil_image = pil_image.resize((self.ui.ImgView.width(), self.ui.ImgView.height()), Image.LANCZOS)
        qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.width * 3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.gradScene = QGraphicsScene()
        self.gradScene.addItem(QGraphicsPixmapItem(pixmap))

        #fastCAM data_gen
        result_image = gradcam.get_fastcam()
        pil_image = Image.fromarray((result_image * 255).astype(np.uint8))
        #rescle the gradcam back to original image size
        pil_image = pil_image.resize((self.ui.ImgView.width(), self.ui.ImgView.height()), Image.LANCZOS)
        # Convert PIL Image to QImage
        qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.width, QImage.Format_Grayscale8)
        pixmap = QPixmap.fromImage(qimage)
        self.fastScene = QGraphicsScene()
        self.fastScene.addItem(QGraphicsPixmapItem(pixmap))

        #guidedBackProp data_gen
        _cam = GuidedBackpropExplainer(self.model)
        result_image = _cam.explain(self.transformed_image)
        result_image = result_image.squeeze().transpose(1, 2, 0)
        pil_image = Image.fromarray((result_image * 255).astype(np.uint8))
        #rescle the gradcam back to original image size
        pil_image = pil_image.resize((self.ui.ImgView.width(), self.ui.ImgView.height()), Image.LANCZOS)
        # Convert PIL Image to QImage
        qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.width * 3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.guidedScene = QGraphicsScene()
        self.guidedScene.addItem(QGraphicsPixmapItem(pixmap))

        #IG data_gen
        ig = IG(self.model)
        result = ig.get_ig(self.transformed_image)
        img_arr = ig.get_ig_img()
        pil_image = Image.fromarray(img_arr)
        #rescle the gradcam back to original image size
        pil_image = pil_image.resize((self.ui.ImgView.width(), self.ui.ImgView.height()), Image.LANCZOS)
        # Convert PIL Image to QImage
        qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.width * 3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.igScene = QGraphicsScene()
        self.igScene.addItem(QGraphicsPixmapItem(pixmap))

        #Saliency data_gen
        saliency = SaliencyAttribution(self.model)
        result = saliency.attribute(self.transformed_image)
        img_arr = saliency.get_saliency_img()
        pil_image = Image.fromarray(img_arr)
        #rescle the gradcam back to original image size
        pil_image = pil_image.resize((self.ui.ImgView.width(), self.ui.ImgView.height()), Image.LANCZOS)
        # Convert PIL Image to QImage
        qimage = QImage(pil_image.tobytes(), pil_image.width, pil_image.height, pil_image.width * 3, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(qimage)
        self.saliencyScene = QGraphicsScene()
        self.saliencyScene.addItem(QGraphicsPixmapItem(pixmap))

        self.data_generated.emit()


    def GradcamViewer(self):
        self.ui.CamView.setScene(self.gradScene)  
        self.ui.CamLable.setText("CAM View : GradCAM")
        self.resizeEvent(None)
    
    def FastcamViewer(self):
        self.ui.CamView.setScene(self.fastScene)
        self.ui.CamLable.setText("CAM View : FastCAM")
        self.resizeEvent(None)
    
    def guidedBackPropViewer(self):
        self.ui.CamView.setScene(self.guidedScene)
        self.ui.CamLable.setText("CAM View : Guided Backprop")
        self.resizeEvent(None)
    
    def igView(self):
        self.ui.CamView.setScene(self.igScene)
        self.ui.CamLable.setText("CAM View : Integrated Gradients")
        self.resizeEvent(None)
    
    def saliencyView(self):
        self.ui.CamView.setScene(self.saliencyScene)
        self.ui.CamLable.setText("CAM View : Saliency")
        self.resizeEvent(None)
        
    def resizeEvent(self, event):
        if self.ui.ImgView.scene() and self.ui.ImgView.scene().items():
            self.ui.ImgView.fitInView(self.ui.ImgView.scene().itemsBoundingRect(), Qt.KeepAspectRatio)
        if self.ui.CamView.scene() and self.ui.CamView.scene().items():
            self.ui.CamView.fitInView(self.ui.CamView.scene().itemsBoundingRect(), Qt.KeepAspectRatio)
        super().resizeEvent(event)  