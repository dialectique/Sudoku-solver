from setuptools import find_packages
from setuptools import setup

# list dependencies from file
with open('requirements.txt') as f:
    content = f.readlines()
requirements = [x.strip() for x in content if 'git+' not in x]

setup(name='sudokuapp',
      version="1.0",
      description="package for sudoku app solving",
      packages=find_packages(),
      install_requires=requirements)
