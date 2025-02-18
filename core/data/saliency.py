import torch
from captum.attr import Saliency
from core import utils

class SaliencyAttribution:
    def __init__(self, model):
        self.model = model
        self.saliency = Saliency(model.model)

    def attribute(self, inputs):
        attributions = self.saliency.attribute(inputs, target=self.model.predict_max(inputs).item())
        img_data  = attributions
        self.ig_image = utils.tensor2imgTensor(img_data.detach().numpy())
        return attributions

    def get_saliency_img(self):
        return self.ig_image
    