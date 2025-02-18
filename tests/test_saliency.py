import pytest
import torch
import numpy as np
from core.data.saliency import SaliencyAttribution
from core.model import Model
from PIL import Image

@pytest.fixture
def setup():
    model = Model()
    model.load('./tests/model.pth')
    image = Image.open('./images/tests/base_test.jpg')
    image = model.transform('./images/tests/base_test.jpg')
    return image, model

@pytest.fixture
def saliency(setup):
    image,model = setup
    return SaliencyAttribution(model), image

def test_ig(saliency):
    saliency, image = saliency
    result = saliency.attribute(image)
    assert isinstance(result, torch.Tensor)
    assert result.shape == (1,3,224, 224)
    img_arr = saliency.get_saliency_img()
    Image.fromarray(img_arr).save('./images/tests/result_saliency.png')
