from .get_tags import get_tags

def tags(md_file_name, helpers):

    if helpers.file_exist(md_file_name):
        print(get_tags(md_file_name))
    else:
        print(helpers.colors.error('the ' + md_file_name + ' file does not yet exist'))
        print(helpers.colors.warning('Tip, you can create a new note file with: pynotes -nf'))