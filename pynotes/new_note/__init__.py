import os
from .write_md_file import write_md_file

def new_note(md_file_name, helpers):

    if helpers.file_exist(md_file_name):
        print(helpers.colors.warning('The file ' + md_file_name + ' already exist in '  + os.getcwd()))
    else:
        write_md_file(md_file_name)
        print(helpers.colors.success('A new note file called ' + md_file_name + ' was successfully created in ' + os.getcwd()))