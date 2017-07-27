<p align="center">
  <br/>
  <img src="https://raw.githubusercontent.com/ajnebro/pyMSAScoring/master/resources/pymsa.png" alt="PyMSA">
  <br/>
</p>

# Scoring Multiple Sequence Alignments with Python
[![Build Status](https://travis-ci.org/ajnebro/pyMSAScoring.svg?branch=master)](https://travis-ci.org/ajnebro/pyMSAScoring)
[![PyPI](https://img.shields.io/pypi/l/pyMSAScoring.svg)]()
[![PyPI](https://img.shields.io/pypi/v/pyMSAScoring.svg)]()

PyMSA is an open source software tool aimed at providing a number of scores for
multiple sequence alignment (MSA) problems. This project is a development of the students of the
third course students of the degree on Bioinformatics of the E.T.S. de Ingeniería Informática
of the University of Málaga.

## Features
The scores that are currently available are:
* Sum of pairs,
* Star,
* Minimum entropy,
* Percentage of non-gaps *and*
* Percentage of totally conserved columns.

## Downloading
To download PyMSA just clone the Git repository hosted in GitHub:
```bash
$ git clone https://github.com/ajnebro/pyMSA.git
$ python setup.py install
```

Alternatively, you can install with pip:
```bash
$ pip install pyMSA
```

## Requirements
PyMSA has been developed with Python 3.6.0 :: [Anaconda](https://www.continuum.io) 4.3.0 (x86_64).

To install all dependencies use:
```bash
$ pip install -r requirements.txt
```

## Usage
An example of running all the included scores is located in the [`scoringExample`](pymsa/scoringExample.py) file.


## History
### Last changes (July 2017)
* `pyMSAScoring` project is now renamed to `pyMSA`!
* All the scores are now computed using a **list of sequences instead of a list of pairs**.
* Tests for [Percentage of non-gaps](pymsa/test/test_scoring.py) added.

## Authors
### Active development team 
* Antonio Benítez <antonio.b@uma.es>
* Antonio J. Nebro <antonio@lcc.uma.es>

### Thanks to
* Maria José Muñoz - Project Manager
* Miguel Ángel Gallardo - Developer of the Star score
* Daniel Torres - Developer of the Star code
* René Betancor - Developer of the Sum of Pairs score
* Pablo Rodríguez - Developer of the Entropy score
* Guillermo López - Developer of the Entropy score
* Juan Ignacio Álvarez - Developer of the of Non-Gaps score

## License
This project is licensed under the terms of the MIT - see the [LICENSE](https://github.com/ajnebro/pyMSAScoring/blob/master/LICENSE) file for details.
