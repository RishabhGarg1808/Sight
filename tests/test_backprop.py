import torch
from torchvision import transforms
import pytest
import numpy as np
from pytorch_grad_cam.utils.image import show_cam_on_image
from core.data.guided_backprop import GuidedBackpropExplainer
from core.model import Model
from PIL import Image

@pytest.fixture
def setup():
    model = Model()
    model.load('./tests/model.pth')
    image = Image.open('./images/tests/base_test.jpg')
    image = model.transform('./images/tests/base_test.jpg')
    return image, model

def test_backprop(setup):
    image, model = setup
    _cam = GuidedBackpropExplainer(model)
    result_image = _cam.explain(image)
    assert isinstance(result_image, np.ndarray)
    assert result_image.shape == (1 , 3 ,224, 224)
    result_image = result_image.squeeze().transpose(1, 2, 0)
    Image.fromarray(result_image).save('./images/tests/result_backProp.png')