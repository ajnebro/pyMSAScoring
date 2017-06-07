
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

    author='Antonio Jseus Nebro',
    author_email='ajnebro@uma.es',
    author0='Maria Jose Muñoz',
    author_email0='marmungon@uma.es',
    author1='Daniel Torres',
    author_email1='dantorram@uma.es',
    author2='Miguel Angel Gallardo',
    author_email2='miggalrui@uma.es',
    author3='Antonio Benitez',
    author_email3='antonio.b@uma.es',
    author4='Rene Betancor',
    author_email4='renebetsar@uma.es',
    author5='Juan Ignacio Alvarez',
    author_email5='juaalvare@uma.es',
    author6='Guillermo Lopez',
    author_email6='guilopgar@uma.es',
    author7='Pablo Rodriguez',
    author_email7='pabrod@uma.es',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience:: Science / Research',

        'Programming Language :: Python :: 3.6'
    ],

    packages=find_packages(exclude=['test']),

)