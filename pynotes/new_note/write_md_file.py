def write_md_file(md_file_name):

    md_file = open(md_file_name, 'w+')

    heading = '# Notes: ' + str(md_file_name) + '\n\n'
    tags    = '> Tags: \n\n'
    links   = '## Links: \n\n'

    md_file.write(heading + tags + links)
    md_file.close()

    return md_file