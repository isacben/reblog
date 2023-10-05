import os
import sys

from typing import List

def get_html_template() -> str:
    home_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = home_path + '/partials/template.html'
    with open(file_path, 'r') as f:
        return f.read()
