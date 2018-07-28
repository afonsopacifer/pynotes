from setuptools import setup, find_packages

setup(name='pynotes',
      version='0.1.2',
      description='Create daily notes/log with markdown.',
      long_description='Create daily notes/log with markdown.',
      url='http://github.com/afonsopacifer/pynotes',
      author='Afonso Pacifer',
      author_email='afonsopacifer@live.com',
      license='MIT',
      packages=find_packages(),
      entry_points = {
          'console_scripts': [
              'pynotes = pynotes.__main__:main'
        ]
      },
      zip_safe=False)