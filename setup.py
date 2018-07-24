from setuptools import setup

setup(name='pynotes',
      version='0.1.0',
      description='Create daily notes/log with markdown.',
      url='http://github.com/afonsopacifer/py_notes',
      author='Afonso Pacifer',
      author_email='afonsopacifer@live.com',
      license='MIT',
      packages=['pynotes'],
      entry_points = {
          'console_scripts': [
              'pynotes = pynotes.__main__:main'
        ]
      },
      zip_safe=False)