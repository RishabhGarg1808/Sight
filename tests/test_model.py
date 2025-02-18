import ast
import pytest
import torch
from unittest import mock
from core.model import Model
from torchvision.models import resnet152


class MockUtils:
    @staticmethod
    def check_file_exists(path):
        # Mock behavior: Assume all files exist
        return True

class MockDownloader:
    class MockDownloadFactory:
        @staticmethod
        def download(url, path):
            
            pass


@pytest.fixture
def mock_utils(monkeypatch):
    monkeypatch.setattr('utils.check_file_exists', MockUtils.check_file_exists)

@pytest.fixture
def mock_downloader(monkeypatch):
    monkeypatch.setattr('downloader.DownloadFactory', MockDownloader.MockDownloadFactory)

@pytest.fixture
def model():
    return Model()

def test_load_model_existing_file(model, mock_utils):
    path = './tests/model.pth'
    loaded_model = model.load(path)
    assert loaded_model is not None, f"Failed to load model from {path}"

def test_load_model_non_existing_file(model, mock_utils, mock_downloader):
    path = './tests/model.pth'
    loaded_model = model.load(path)
    assert loaded_model is not None, f"Failed to load model from {path}"

def test_predict_max(model, mock_utils):
    path = './tests/model.pth'
    model.load(path)
    img = './images/tests/base_test.jpg'
    predictions = model.predict_max(img)
    assert predictions is not None, f"Failed to get predictions from {path}"

def test_predict(model, mock_utils):
    path = './tests/model.pth'
    model.load(path)
    img = './images/tests/base_test.jpg'
    predictions = model.predict(img)
    assert predictions is not None, f"Failed to get predictions from {path}"

def test_decode_predictions(model):
    path = './tests/model.pth'
    model.load(path)
    img = './images/tests/base_test.jpg'
    predictions = model.predict_max(img)
    
    with open('./core/default_labels.txt', 'r') as f:
        data = f.read()
        class_names = ast.literal_eval(data)
    
    decoded = model.decode_predictions(predictions)
    assert decoded == class_names[predictions.topk(1).indices.squeeze().tolist()], f"Failed to decode predictions: {decoded}"