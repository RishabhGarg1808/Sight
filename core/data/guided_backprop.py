import numpy as np
import torch
from captum.attr import GuidedBackprop

class GuidedBackpropExplainer:
    def __init__(self, model):
        self.model = model
        self.guided_backprop = GuidedBackprop(self.model.model)

    def explain(self, inputs):
        self.model.model.eval()
        attributions = self.guided_backprop.attribute(inputs, target=self.model.predict_max(inputs).item())
        attributions = attributions.detach().cpu().numpy()
        attributions = (attributions * 255).astype(np.uint8)
        return attributions

   