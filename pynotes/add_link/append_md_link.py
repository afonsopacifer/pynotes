from .format_link import format_link

def append_md_link(md_file_name):

    md_file = open(md_file_name, 'a')

    link_title = str(input('Enter a link title: '))
    link_url   = str(input('Enter a link url: '))

    md_link = format_link(link_title, link_url)

    md_file.write(md_link)
    md_file.close()

    return md_link