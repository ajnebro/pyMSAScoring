
from setuptools import setup, find_packages
from codecs import open
from os import path

setup(
    name='pyMSAScoring',

    version='0.1.2',

    description='Scoring Multiple Sequence Alignments with Python',

    url='https://github.com/ajnebro/pyMSAScoring',

    author='Maria Jose Muñoz, Antonio Benitez, Pablo Rodriguez, Antonio J. Nebro',
    author_email='ajnebro@uma.es',

    license='MIT',

    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Science/Research',

        'License :: OSI Approved :: MIT License',

        'Topic :: Scientific/Engineering :: Bio-Informatics',

        'Programming Language :: Python :: 3.6'
    ],

    packages=find_packages(exclude=['*Test']),
)