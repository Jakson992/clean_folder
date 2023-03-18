from setuptools import setup, find_namespace_packages

setup(name='clean-folder',
      author='Yevhenii Petrenko',
      version='0.1.0',
      packages=find_namespace_packages(),
      license='MIT',
      entry_points={'console_scripts': ['clean-folder=clean_folder.clean:main']}
      )
