import os
import sys

from typing import List

def get_header() -> str:
    home_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = home_path + '/partials/header.html'
    with open(file_path, 'r') as f:
        return f.read()

def get_footer() -> str:
    home_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = home_path + '/partials/footer.html'
    with open(file_path, 'r') as f:
        return f.read()
