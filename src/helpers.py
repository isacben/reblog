import os
import sys
import markdown
import tomllib

from bs4 import BeautifulSoup

from typing import List

def get_html_template() -> str:
    home_path = os.path.dirname(os.path.abspath(sys.argv[0]))
    file_path = home_path + '/partials/template.html'
    with open(file_path, 'r') as f:
        return f.read()
    
def insert_side_bar(dirname: str, html_string: str) -> str:
    # check if there is content for a sidebar
    if os.path.exists(dirname + '/md/_sidebar.md'):
        with open(dirname + '/md/_sidebar.md', 'r') as f:
            sidebar = f.read()
        
        html_string = html_string.replace('%reblog-sidebar%', markdown.markdown(sidebar))
        html_string = format_post(html_string)
        return html_string
    else:
        return ''

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

            posts += """
                <div class="col">
                    <div class="card">
                """
            
            try:
                image = soup.find('img')['src']
                posts += f'<img src="{image}" class="card-img-top" alt="...">'
            except:
                pass

            posts += '<div class="card-body">'
            posts += str(title)

            try:
                text = soup.find('p').get_text()
                posts += '<p class="card-text">' + text + '</p>'
            except:
                print(f'File <{md_file}> had no paragraphs.')
            
            link_filename = md_file.split(".")[0]
            posts += f'<a href="{link_filename}.html" class="stretched-link">Read more</a>'
            posts += """
                        </div>
                    </div>
                </div>
            """
    
    posts += '</div>'

    html_string = html_string.replace("%reblog-content%", posts)

    with open(directory + "/site.toml", "rb") as f:
        site_conf = tomllib.load(f)

    html_string = html_string.replace("%reblog-title%", site_conf['name'])
    html_string = html_string.replace("%reblog-navbar-title%", site_conf['name'])

    html_string = insert_side_bar(directory, html_string)

    output = directory + '/html/index.html'

    with open(output, 'w') as f:
        f.write(html_string)

def format_post(html_string: str) -> str:
    soup = BeautifulSoup(html_string, "html.parser")

    # format images in the post
    images = soup.find_all('img')
    for image in images:
        image['class'] = 'img-fluid'
    
    return str(soup)