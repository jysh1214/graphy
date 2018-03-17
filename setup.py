from setuptools import setup, find_packages

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='pygraph',
    version='0.1',
    description='Lite package for graph',
    long_description=readme,
    author='jysh1214',
    author_email='jyxemperor@gmail.com',
    url='https://github.com/jysh1214/graphy',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)
