def file_exist(file_name):
    try:
        open(file_name, "r")
        return True
    except IOError:
        return False