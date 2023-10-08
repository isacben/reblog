# reblog

A simple tool to create a blog as a static website with no database, using markdown files.

## Requirements

1. Markdown
2. Beautifulsoup

## Installation

1. Clone this repo
2. Create a virtual environment
3. Install `Markdown` and `Beautifulsoup`

## Usage

First create a directory for your blog. Inside, create the following sub directories:

- md: create your posts in this directory, using markdown format
- html: this tool will generate the static pages and place them here
- img: store the images for your posts here

Now, create your first post by adding an md file. For example, `your-post.md`.

You will also need to create the file `_sidebar.md`. Add any information you want to present in the sidebar of your blog.

Once you have an md file and the sidebar, generate the html version  of your blog running this command:

```
python3 src/main.py file /path/to/your/blog-site/md/your-post.md
```

The first argument, is the command `file`. The second argument, is the path to the markdown file that is your post.

After running this command, your site file structure will look like this:

- Your blog site directory
    - md
        - your-post.md
        - _sidebar.md
    - html
        - index.html
        - your-post.html
    - img
        - your-post-image-if-you-added-one.png

Finally, upload the `html` and `img` directories to your web server.



