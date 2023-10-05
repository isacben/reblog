import os
import sys
import markdown
from bs4 import BeautifulSoup

from typing import List

def get_html_template() -> str:
    home_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = home_path + '/partials/template.html'
    with open(file_path, 'r') as f:
        return f.read()

def update_home_page(directory: str) -> None:
    html_string = get_html_template()

    md_files = os.listdir(directory + '/md')
    posts = """
        <div class="row row-cols-1 row-cols-md-3 g-4">
    """

    for md_file in md_files:
        if not md_file.startswith('_'):
            with open(directory + '/md/' + md_file) as f:
                content_html_string = markdown.markdown(f.read())

                soup = BeautifulSoup(content_html_string, "html.parser")
                title = soup.find('h1')
                title.name = 'h5'

                text = soup.find('p').get_text()

                posts += """
                    <div class="col">
                        <div class="card">
                            <img src="..." class="card-img-top" alt="...">
                            <div class="card-body">
                """
                posts += str(title)
                posts += '<p class="card-text">' + text + '</p>'
                posts += '<a href="#" class="stretched-link">Read more</a>'
                print(title)
                posts += """
                            </div>
                        </div>
                    </div>
                """
    
    posts += '</div>'

    html_string = html_string.replace("%reblog-content%", posts)

    output = directory + '/html/index.html'

    with open(output, 'w') as f:
        f.write(html_string)