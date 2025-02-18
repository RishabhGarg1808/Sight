import os
import numpy as np
from PIL import Image

def check_file_exists(path):
    if os.path.exists(path):
        return os.path.abspath(path)
    return None

def check_dir_exists(path):
    return os.path.isdir(path)

def create_dir(path):
    try:
        os.makedirs(path)
        return True
    except Exception as e:
        print(f"Error creating directory: {e}")
        return False

def delete_file(path):
    try:
        os.remove(path)
        return True
    except Exception as e:
        print(f"Error deleting file: {e}")
        return False

def delete_dir(path):
    try:
        os.rmdir(path)
        return True
    except Exception as e:
        print(f"Error deleting directory: {e}")
        return False

def tensor2imgTensor(tensor):
    tensor *= 255
    tensor = np.array(tensor, dtype=np.uint8)
    if np.ndim(tensor)>3:
        assert tensor.shape[0] == 1
        tensor = tensor[0]
    tensor = tensor.squeeze().transpose(1, 2, 0)  # Reshape to (224, 224, 3)
    tensor = (tensor * 255).astype(np.uint8) 
    return tensor