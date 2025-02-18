from torchvision import transforms
import pytest
import numpy as np
from pytorch_grad_cam.utils.image import show_cam_on_image
from core.data.gradcam import GradCAM
from core.model import Model
from PIL import Image

@pytest.fixture
def setup():
    model = Model()
    model.load('./tests/model.pth')
    image = Image.open('./images/tests/base_test.jpg')
    image = model.transform('./images/tests/base_test.jpg')
    return image, model

def test_fastcam(setup):
    image, model = setup
    grad_cam = GradCAM(model, image)
    result_image = grad_cam.fast_cam()
    assert isinstance(result_image, np.ndarray)
    assert result_image.shape == (224, 224)
    Image.fromarray((result_image * 255).astype(np.uint8)).save('./images/tests/result_fastcam.png')

def test_grad_cam(setup):
    image, model = setup
    grad_cam = GradCAM(model, image)
    heatmap , result_image = grad_cam.get_gradcam()
    assert isinstance(result_image, np.ndarray)
    assert result_image.shape == (224, 224 , 3 )
    Image.fromarray((result_image * 255).astype(np.uint8)).save('./images/tests/result_gradcam.png')