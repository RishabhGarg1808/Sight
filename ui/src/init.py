import torch 
from torchvision.models import resnet50 ,ResNet152_Weights
from ..init_ui import Ui_Init
from PySide6.QtWidgets import QSplashScreen, QProgressBar
from PySide6.QtGui import QPixmap, QGuiApplication
from PySide6.QtCore import Qt, Signal, Slot, QEventLoop, QTimer

from core.model import Model
from core.downloader import DownloadFactory
from core.utils import check_file_exists ,check_dir_exists ,create_dir

class LoadingSplashScreen(QSplashScreen):
    download_finished = Signal()
    model_loaded = Signal(Model)
    def __init__(self):
        super().__init__()
        self.ui = Ui_Init()
        self.ui.setupUi(self)
        self.pixmap = QPixmap("Resources/logo.png")
        scaled_pixmap = self.pixmap.scaled(200,200, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.ui.logo.setPixmap(scaled_pixmap)
        self.ui.progressBar.setRange(0, 0)
        self.download_finished.connect(self.load_model)
        self.resize(400, 300)
        self.show()
        self.center()
        self.default_destination = "~/.sight/models"
        if not check_dir_exists(self.default_destination):
            create_dir(self.default_destination)


    def center(self):
        screen = QGuiApplication.primaryScreen()
        screen_geometry = screen.geometry()
        size = self.geometry()
        self.move((screen_geometry.width() - size.width()) // 2, (screen_geometry.height() - size.height()) // 2)

    def init(self):
        self.show()
        self.center()
        self.ui.progressStats.setText("Initializing ....")
        DEFAULT_WEIGHT = ResNet152_Weights.IMAGENET1K_V2
        self.downloader = DownloadFactory().get_downloader(DEFAULT_WEIGHT)
        self.wait_for_timer(2000)
        self.download()
        self.wait_for_timer(1200)
        self.download()
        self.wait_for_timer(1000)
        self.ui.progressStats.setText("Loading ui")
        self.wait_for_timer(1200)
        self.load_model()

    def load_model(self):
        model = Model()
        model.load(self.model_path)
        self.model_loaded.emit(model)
        self.destroy()


    def download(self):
        if check_file_exists(self.default_destination + "/" +self.downloader.weight_name):
            self.ui.progressStats.setText("Weights Already Exist. Loading ....")
            self.model_path = self.default_destination + "/" + self.downloader.weight_name 
            self.wait_for_timer(400)
        else:
            self.ui.progressStats.setText(f"Downloading Default Weights ( {self.downloader.file_size} mb)")
            self.downloader.download_progress.connect(self.update_bar)
            self.downloader.download_finished.connect(self.download_finished.emit)
            self.model_path = self.downloader.download(self.default_destination + "/" + self.downloader.weight_name )

    @Slot()
    def update_bar(self,value):
        self.ui.progressBar.setRange(0, 100)
        self.ui.progressBar.setValue(value)
    @Slot()
    def load_finished(self):
        self.hide()

    def mousePressEvent(self, arg__1):
        pass

    def wait_for_timer(self,timeout):
        loop = QEventLoop()
        timer = QTimer()
        timer.setSingleShot(True)
        timer.timeout.connect(loop.quit)
        timer.start(timeout)
        loop.exec()
    
