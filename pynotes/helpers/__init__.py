from .file_exist import file_exist

class helpers:

    def file_exist(file_name):
        return file_exist(file_name)

    class colors:

        def success(text):
            return '\033[92m' + text

        def warning(text):
            return '\033[93m' + text

        def error(text):
            return '\033[91m' + text