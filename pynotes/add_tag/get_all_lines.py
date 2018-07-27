def get_all_lines(md_file_name):

    md_file = open(md_file_name, 'r')
    md_file_lines = md_file.readlines()
    md_file.close()

    return md_file_lines