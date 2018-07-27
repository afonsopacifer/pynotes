import copy

def get_all_lines(md_file_name):
    md_file = open(md_file_name, 'r')
    md_file_lines = md_file.readlines()
    md_file.close()
    return md_file_lines

def get_tag_line(md_file_lines):
    md_tag_line = md_file_lines[2]
    return md_tag_line[:-1] # Remove the last \n

def format_tag(tag_name):
    md_tag_name = '`' + tag_name + '`'
    return md_tag_name

def update_tag_line(md_file_lines, md_tag_name):
    md_tag_line = get_tag_line(md_file_lines)
    md_file_lines_updated = copy.deepcopy(md_file_lines)
    md_file_lines_updated[2] = md_tag_line + md_tag_name + ' \n'
    return md_file_lines_updated

def append_md_tag(md_file_name):

    tag_name    = str(input('Enter a tag name: '))
    md_tag_name = format_tag(tag_name)

    md_file_lines         = get_all_lines(md_file_name)
    md_file_lines_updated = update_tag_line(md_file_lines, md_tag_name)

    md_file = open(md_file_name, 'w')
    md_file.writelines(md_file_lines_updated)
    md_file.close()

    return get_tag_line(md_file_lines_updated)