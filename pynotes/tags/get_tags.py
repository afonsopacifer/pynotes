def get_tags(md_file_name):

    md_file = open(md_file_name, 'r')

    md_tag_line = md_file.readlines()[2]
    md_tags = md_tag_line[8:]

    md_file.close()

    return md_tags