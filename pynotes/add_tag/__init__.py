from .append_md_tag import append_md_tag

def add_tag(md_file_name , helpers):

    if helpers.file_exist(md_file_name):
        append_md_tag(md_file_name)
        print(helpers.colors.success('New tag successfully annotated'))
    else:
         print(helpers.colors.error('the ' + md_file_name + ' file does not yet exist'))
         print(helpers.colors.warning('Tip, you can create a new note file with: pynotes -nf'))