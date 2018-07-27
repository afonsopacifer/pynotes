from .format_tag import format_tag
from .get_all_lines import get_all_lines
from .update_tag_line import update_tag_line
from .get_tag_line import get_tag_line

def append_md_tag(md_file_name):

    tag_name    = str(input('Enter a tag name: '))
    md_tag_name = format_tag(tag_name)

    md_file_lines         = get_all_lines(md_file_name)
    md_file_lines_updated = update_tag_line(md_file_lines, md_tag_name)

    md_file = open(md_file_name, 'w')
    md_file.writelines(md_file_lines_updated)
    md_file.close()

    return get_tag_line(md_file_lines_updated)