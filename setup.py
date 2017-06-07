
from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='pyMSAScoring',

    version='0.1',

    description='Scoring Multiple Sequence Alignments with Python',
    long_description=long_description,

    url='https://github.com/ajnebro/pyMSAScoring',

    author='Maria Jose Muñoz, Antonio Benitez, Pablo Rodriguez, Antonio J. Nebro',
    author_email='ajnebro@uma.es',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience:: Science / Research',

        'Programming Language :: Python :: 3.6'
    ],

    packages=find_packages(exclude=['test']),

)