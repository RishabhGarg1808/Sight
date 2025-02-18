import unittest
import pytest
import sys
import os

# Add the parent directory to sys.path to ensure imports work correctly
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Add the directory containing the 'utils' module to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'core')))

# Discover and run all unittest tests
loader = unittest.TestLoader()
model_suite = loader.discover(start_dir='.', pattern='test*.py')
runner = unittest.TextTestRunner()
runner.run(model_suite)

# Discover and run all pytest tests
pytest.main()