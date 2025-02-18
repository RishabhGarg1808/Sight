import requests
from torchvision.models import ResNet152_Weights
from PySide6.QtCore import Signal, Slot, QObject

class Downloader(QObject):
    download_progress = Signal(int)
    download_finished = Signal()
    
    def __init__(self, url):
        super().__init__()
        self.url = url
        self.file_size = 230
        self.weight_name = "resnet152-f82ba261.pth" if  url == "https://download.pytorch.org/models/resnet152-f82ba261.pth" else "resnet152-394f9c45.pth"
    

    def download(self, destination):
        try:
            response = requests.get(self.url, stream=True)
            response.raise_for_status()
            total_length = response.headers.get('content-length')
            if total_length is None:  # No content length header
                with open(destination, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
            else:
                total_length = int(total_length)
                downloaded = 0
                with open(destination, 'wb') as file:
                    for chunk in response.iter_content(chunk_size=8192):
                        downloaded += len(chunk)
                        file.write(chunk)
                        progress = int(100 * downloaded / total_length)
                        self.download_progress.emit(progress)
                        if progress == 100:
                            self.download_finished.emit()
            print(f"Downloaded successfully to {destination}")
            return destination
        except requests.exceptions.RequestException as e:
            print(f"Error downloading file: {e}")
            return None

class DownloadFactory:
    def get_downloader(self, WeightType):
        switcher = {
            ResNet152_Weights.IMAGENET1K_V2 : Downloader("https://download.pytorch.org/models/resnet152-f82ba261.pth"),
            ResNet152_Weights.IMAGENET1K_V1 : Downloader("https://download.pytorch.org/models/resnet152-394f9c45.pth") 
        }
        return switcher.get(WeightType, None)

