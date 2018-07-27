import argparse
import time
from .new_note import new_note
from .add_link import add_link
from .add_tag import add_tag
from .helpers import helpers
from .read import read
from .links import links
from .tags import tags

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-nf', '--new_file', help='Create a note file.',      action='store_true')
    parser.add_argument('-al', '--add_link', help='Add a new link.',          action='store_true')
    parser.add_argument('-at', '--add_tag',  help='Add a new tag.',           action='store_true')
    parser.add_argument('-r',  '--read',     help='Read note file and show.', action='store_true')
    parser.add_argument('-l',  '--links',    help='Get all links and show.',  action='store_true')
    parser.add_argument('-t',  '--tags',     help='Get all tags and show.',   action='store_true')
    args = parser.parse_args()

    file_name = time.strftime('%d-%m-%Y')
    md_file_name = file_name + '.md'

    # -nf, --new_file
    if args.new_file: new_note(md_file_name, helpers)

    # -al, --add_link
    elif args.add_link: add_link(md_file_name, helpers)

    # -at, --add_tag
    elif args.add_tag: add_tag(md_file_name, helpers)

    # -r, --read
    elif args.read: read(md_file_name, helpers)

    # -l, --links
    elif args.links: links(md_file_name, helpers)

    # -t, --tags
    elif args.tags: tags(md_file_name, helpers)

if __name__ == '__main__':
    main()