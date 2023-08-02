from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='0.0.1',
      description='Clean Folder_kas',
      author='Andrii Korniev',
      author_email='KorenbAS78@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.main:start']}
      )
