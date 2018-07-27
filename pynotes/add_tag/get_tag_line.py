def get_tag_line(md_file_lines):
    md_tag_line = md_file_lines[2]
    return md_tag_line[:-1] # Remove the last \n