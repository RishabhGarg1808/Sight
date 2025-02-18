from ..main_window_ui import Ui_MainWindow
from PySide6 .QtWidgets import QMainWindow, QFileDialog, QGraphicsScene,QGraphicsPixmapItem
from PySide6.QtCore import Slot, Qt , QSize ,Signal ,QThread ,QObject
from PySide6.QtGui import QIcon, QPixmap 
from core.model import Model
import torch ,numpy as np
from PIL import Image
from ui.src.view import View
from ui.waiting_spinner import WaitingSpinner

class Worker(QObject):
    finished = Signal()
    data_generated = Signal()

    def __init__(self, view):
        super().__init__()
        self.view = view

    def run(self):
        self.view.data_gen()
        self.data_generated.emit()
        self.finished.emit()

class MainWindow(QMainWindow):
    imageLoaded = Signal()
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.Settings.setIcon(QIcon("Resources/settings.png"))
        self.ui.Settings.setIconSize(QSize(30,30))
        self.ui.More.setIcon(QIcon("Resources/plus.png"))
        self.ui.More.setIconSize(QSize(30,30))
        self.ui.LoadBtn.clicked.connect(self.open_image)
        self.imageLoaded.connect(self.on_imageLoad)
        self.ui.More.clicked.connect(self.cycle_View)
        self.ui.GuideBtn.hide()
        self.ui.Settings.hide()

        self.waitSpinner = WaitingSpinner(self.ui.centralwidget)

        #some Global varibales to make things easier, they are used later
        self.Image = None
        self.model = None
        self.gradcam = None
        self.viewCounter = 0
        self.View = None

    def open_image(self):
        file, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Images (*.png *.jpg *.jpeg)")
        self.Image = file
        if file:
            self.ui.ImgView.setScene(None)
            self.ui.CamView.setScene(None)
            pixmap = QPixmap(file)
            scene = QGraphicsScene()
            scene.addItem(QGraphicsPixmapItem(pixmap))
            self.ui.ImgView.setScene(scene)
            self.resizeEvent(None)
            self.View = View(self.model, self.Image, self.ui)
            self.View.data_generated.connect(self.on_Datagen)
            self.imageLoaded.emit()
    

    def resizeEvent(self, event):
        if self.ui.ImgView.scene() and self.ui.ImgView.scene().items():
            self.ui.ImgView.fitInView(self.ui.ImgView.scene().itemsBoundingRect(), Qt.KeepAspectRatio)
        if self.ui.CamView.scene() and self.ui.CamView.scene().items():
            self.ui.CamView.fitInView(self.ui.CamView.scene().itemsBoundingRect(), Qt.KeepAspectRatio)
        super().resizeEvent(event)
    
    #Slots for various functions and activites
    @Slot(Model)
    def on_modelLoad(self,model):
        self.model = model
        print("Model Loaded")
    
    @Slot()
    def on_Datagen(self):
        self.waitSpinner.stop()

    @Slot()
    def on_imageLoad(self):
        transformed_image = self.model.transform(self.Image)
        prediction = self.model.predict(transformed_image)
        torch.nn.functional.softmax(prediction, dim=1)
        confidence, predicted_class = torch.max(prediction, 1)
        decoded_predictions = self.model.decode_predictions(predicted_class)
        confidence =  confidence.item() * 10
        self.ui.Label.setText(f"Prediction: {decoded_predictions} || Confidence: {confidence:.2f}%")

        self.waitSpinner.start()
        self.thread = QThread()
        self.worker = Worker(self.View)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.worker.data_generated.connect(self.View.GradcamViewer)

        self.thread.start()

    @Slot()
    def cycle_View(self):
        if self.viewCounter == 0:
            self.View.FastcamViewer()
            self.viewCounter = 1
        elif self.viewCounter == 1:
            self.View.guidedBackPropViewer()
            self.viewCounter = 2
        elif self.viewCounter == 2:
            self.View.igView()
            self.viewCounter = 3
        elif self.viewCounter == 3:
            self.View.saliencyView()
            self.viewCounter = 4
        elif self.viewCounter == 4:
            self.View.GradcamViewer()
            self.viewCounter = 0