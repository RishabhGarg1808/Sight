#!/bin/bash
# This script is used to generate necessary ui header files

set -e  # Exit immediately if a command exits with a non-zero status
set -u  # Treat unset variables as an error and exit immediately
set -o pipefail  # Prevents errors in a pipeline from being masked

# Generate the header file
pyside6-uic init.ui -o init_ui.py
pyside6-uic main_window.ui -o main_window_ui.py