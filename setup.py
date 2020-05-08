from setuptools import setup

setup(
    name='diversenames',
    url='https://github.com/NikhilBehari/diverse-names',
    author='Nikhil Behari',
    author_email='nikhil@nikhilbehari.com',
    packages=['diversenames'],
    include_package_data=True,
    install_requires=[],
    version='0.1',
    license='MIT',
    description='Generates a random diverse name',
    long_description=open('README.rst').read()
)
