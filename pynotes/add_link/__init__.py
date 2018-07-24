def add_link(file_name):

    md_file_name = str(file_name) + '.md'
    md_file = open(md_file_name, 'a')

    link_title = str(input('Enter a link title: '))
    link_url =  str(input('Enter a link url: '))

    md_link = '[' + link_title + '](' + link_url + ')'
    md_file.write('- ' + md_link + '\n')

    md_file.close()

    print('New link successfully annotated')
    return md_file