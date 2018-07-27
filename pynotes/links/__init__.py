from .get_links import get_links

def links(md_file_name, helpers):

    if helpers.file_exist(md_file_name):
        md_links = get_links(md_file_name)

        for md_link in md_links:
            print(md_link)

    else:
        print(helpers.colors.error('the ' + md_file_name + ' file does not yet exist'))
        print(helpers.colors.warning('Tip, you can create a new note file with: pynotes -nf'))