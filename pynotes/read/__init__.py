def read(md_file_name, helpers):

    if helpers.file_exist(md_file_name):
        md_file = open(md_file_name, 'r')
        print(str(md_file.read()))
        md_file.close()
    else:
        print(helpers.colors.error('the ' + md_file_name + ' file does not yet exist'))
        print(helpers.colors.warning('Tip, you can create a new note file with: pynotes -nf'))