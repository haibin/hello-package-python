from setuptools import setup, find_packages

setup(
    name='hello',
    packages=find_packages(where='src'),
    package_dir={'':'src'},
)