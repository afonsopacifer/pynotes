import copy
from .get_tag_line import get_tag_line

def update_tag_line(md_file_lines, md_tag_name):

    md_tag_line = get_tag_line(md_file_lines)

    md_file_lines_updated = copy.deepcopy(md_file_lines)
    md_file_lines_updated[2] = md_tag_line + md_tag_name + ' \n'

    return md_file_lines_updated