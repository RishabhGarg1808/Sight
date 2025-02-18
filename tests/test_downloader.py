import pytest
import os
from unittest.mock import patch, mock_open

import requests
from core.downloader import Downloader, DownloadFactory
from torchvision.models import ResNet152_Weights

@pytest.fixture
def downloader():
    return Downloader("https://example.com/testfile")

def test_downloader_init(downloader):
    assert downloader.url == "https://example.com/testfile"

@patch("requests.get")
def test_downloader_download_success(mock_get, downloader):
    mock_response = mock_get.return_value
    mock_response.iter_content = lambda chunk_size: [b"test data"]
    mock_response.raise_for_status = lambda: None

    with patch("builtins.open", mock_open()) as mock_file:
        destination = downloader.download("/tmp/testfile")
        mock_file.assert_called_once_with("/tmp/testfile", "wb")
        mock_file().write.assert_called_once_with(b"test data")
        assert destination == "/tmp/testfile"

@patch("requests.get")
def test_downloader_download_failure(mock_get, downloader):
    mock_get.side_effect = requests.exceptions.RequestException("Download error")

    destination = downloader.download("/tmp/testfile")
    assert destination is None

def test_download_factory_get_downloader():
    factory = DownloadFactory()
    downloader_v2 = factory.get_downloader(ResNet152_Weights.IMAGENET1K_V2)
    assert downloader_v2.url == "https://download.pytorch.org/models/resnet152-f82ba261.pth"

    downloader_v1 = factory.get_downloader(ResNet152_Weights.IMAGENET1K_V1)
    assert downloader_v1.url == "https://download.pytorch.org/models/resnet152-394f9c45.pth"

    downloader_none = factory.get_downloader(None)
    assert downloader_none is None