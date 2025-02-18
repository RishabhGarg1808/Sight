import pytest
import torch
import numpy as np
from core.data.integrated_gradients import IG
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
def ig(setup):
    image,model = setup
    return IG(model), image

def test_ig(ig):
    ig, image = ig
    result = ig.get_ig(image)
    assert isinstance(result, torch.Tensor)
    assert result.shape == (1,3,224, 224)
    img_arr = ig.get_ig_img()
    Image.fromarray(img_arr).save('./images/tests/result_ig.png')
