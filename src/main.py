import markdown
import argparse 
import os
import sys
import helpers

from typing import List

def convert_one_file(filename: str) -> None:
    with open(filename, 'r') as f:
        markdown_string = f.read()

    html_string = helpers.get_header()
    html_string += markdown.markdown(markdown_string)
    html_string += helpers.get_footer()

    dirname = os.path.dirname(os.path.dirname(filename))

    if not os.path.exists(dirname + '/html'):
        os.mkdir(dirname + '/html')

    output = dirname + \
        "/html/" + \
        os.path.basename(filename).split('.')[0] + \
        '.html'

    with open(output, 'w') as f:
        f.write(html_string)

def convert_file(args: List[str]) -> None:
    convert_one_file(args.name)

def convert_dir(args: List[str]):
    print("The directory name is:", args.dirname)

def upload(args):
    print("Upload the file or directory:", args.dirname)

def status(args):
    print("Print the working status for directory:", args.path)


def main() -> int:
    parser = argparse.ArgumentParser(prog="reblog", description="static blog generator")
    parser.add_argument('-v', '--version', action='version', version='%(prog)s version 0.1.0')

    subparsers = parser.add_subparsers(help='available commands')

    parser_file = subparsers.add_parser('file', help='convert a file to html')
    parser_file.add_argument('name', help='the file name')
    parser_file.set_defaults(func=convert_file)

    parser_dir = subparsers.add_parser('dir', help='convert all files in a directory to html')
    parser_dir.add_argument('path', help='the path of the directory')
    parser_dir.set_defaults(func=convert_dir)

    parser_upload = subparsers.add_parser('upload', help='upload a file or directory to the server')
    parser_upload.add_argument('name', help='the file or directory name')
    parser_upload.set_defaults(func=upload)

    parser_status= subparsers.add_parser('status', help='show the working tree status')
    parser_status.add_argument('path', help='the directory name')
    parser_status.set_defaults(func=status)

    args = parser.parse_args()
    args.func(args)

    return 0


if __name__ == "__main__":
    exit(main())
