import torch
import torch.nn as nn
import torch.nn.functional as F
from torchvision.models import resnet152 ,ResNet152_Weights
from PIL import Image
from torchvision import transforms
import ast

import core.utils as utils
import core.downloader as downloader

class Model():
    def __init__(self,path=None):
        self.path = path
        self.model = None
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    def load(self,path):
        if(utils.check_file_exists(path)):
            try:
                self.model = resnet152(pretrained=False)
                self.model.to(self.device)
                self.model.load_state_dict(torch.load(path))
                self.path = path
            except Exception as e:
                print(f"Error loading model: {e}")
                return None
        else:
            downloader.DownloadFactory().get_downloader(ResNet152_Weights.IMAGENET1K_V2).download(path)
            try:
                self.model = resnet152(pretrained=False)
                self.model.to(self.device)
                self.model.load_state_dict(torch.load(path))
                self.path = path
            except Exception as e:
                print(f"Error loading model: {e}")
                return None
            return None
        return self.model
    
    def transform(self, img):
        if isinstance(img, str):
            img = Image.open(img).convert('RGB')
        if isinstance(img, torch.Tensor):
            return img.to(self.device)
        transform = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
            transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]),
        ])
        return transform(img).unsqueeze(0).to(self.device)

    def predict_max(self,img):
        if self.model == None:
            return None
        img = self.transform(img)
        self.model.eval()
        with torch.no_grad():
            return torch.argmax(self.model(img), dim=1)
    
    def predict(self,img):
        if self.model == None:
            return None
        img = self.transform(img)
        self.model.eval()
        with torch.no_grad():
            return self.model(img)
    
    
    def decode_predictions(self, index, list='core/default_labels.txt'):
        try:
            list = utils.check_file_exists(list)
        except Exception as e:
            print(f"Error: {e}")
            return None
        with open(list, 'r') as f:
            data = f.read()
            class_names = ast.literal_eval(data)

        return class_names[index.item()]
        
