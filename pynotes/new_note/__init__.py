import os

def new_note(file_name):

    md_file_name = str(file_name) + '.md'
    md_file = open(md_file_name, 'w+')

    md_file.write('# Notes: ' + str(file_name) + '\n\n')
    md_file.write('> Tags: \n\n')
    md_file.write('## Links: \n\n')

    md_file.close()

    print('A new note file called ' + str(file_name) + '.md was created successfully in ' + os.getcwd())
    return md_file

    #todo:
    #subscribe msg
    #erro msg