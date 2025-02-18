import os
import pytest
from core.utils import check_file_exists, check_dir_exists, create_dir, delete_file, delete_dir

@pytest.fixture
def setup_files_and_dirs():
    test_dir = '/tmp/test_dir'
    test_file = '/tmp/test_file.txt'
    if not os.path.exists(test_dir):
        os.makedirs(test_dir)
    with open(test_file, 'w') as f:
        f.write('test')
    yield test_dir, test_file
    if os.path.exists(test_file):
        os.remove(test_file)
    if os.path.exists(test_dir):
        os.rmdir(test_dir)

def test_check_file_exists(setup_files_and_dirs):
    test_dir, test_file = setup_files_and_dirs
    assert check_file_exists(test_file)
    assert not check_file_exists('/tmp/non_existent_file.txt')

def test_check_dir_exists(setup_files_and_dirs):
    test_dir, test_file = setup_files_and_dirs
    assert check_dir_exists(test_dir)
    assert not check_dir_exists('/tmp/non_existent_dir')

def test_create_dir():
    new_dir = '/tmp/new_test_dir'
    assert create_dir(new_dir)
    assert os.path.exists(new_dir)
    os.rmdir(new_dir)

def test_delete_file(setup_files_and_dirs):
    test_dir, test_file = setup_files_and_dirs
    assert delete_file(test_file)
    assert not os.path.exists(test_file)

def test_delete_dir(setup_files_and_dirs):
    test_dir, test_file = setup_files_and_dirs
    assert delete_dir(test_dir)
    assert not os.path.exists(test_dir)
