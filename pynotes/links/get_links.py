def get_links(md_file_name):

    md_file = open(md_file_name, 'r')
    md_file_lines = md_file.readlines()

    md_links = filter(lambda md_line: '- [' in md_line, md_file_lines)

    md_file.close()

    return md_links