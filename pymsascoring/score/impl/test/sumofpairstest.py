import unittest
import logging
from pymsascoring.substitutionmatrix.impl.blosum62 import Blosum62
from pymsascoring.substitutionmatrix.impl.pam250 import PAM250
from pymsascoring.score.impl.sumofpairs import SumOfPairs

__author__  = "Rene Betancor"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__  = "Development"
__email__   = "renebetsar@uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SumOfPairsTestCase(unittest.TestCase):

    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")

    def test_basic_score_of_12_with_PAM250(self):
        logger.info("Test for compute()...")
        matrix = PAM250()
        msa = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        sumofpairs = SumOfPairs(matrix)

        result = sumofpairs.compute(msa)
        expected = 12
        self.assertEqual(expected, result)

    def test_basic_score_of_12_with_BLOSUM62(self):
        logger.info("Test for compute()...")
        matrix = Blosum62()
        msa = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        sumofpairs = SumOfPairs(matrix)

        result = sumofpairs.compute(msa)
        expected = 24
        self.assertEqual(expected, result)

    def test_basic_score_with_gaps_BLOSUM62(self):
        logger.info("Test for compute()...")
        matrix = Blosum62()
        msa = [('ID1',
                 'FA'),
                ('ID2',
                 'A-')]
        sumofpairs = SumOfPairs(matrix)

        result = sumofpairs.compute(msa)
        expected = -10
        self.assertEqual(expected, result)

    def test_only_gaps_with_BLOSUM62(self):
        logger.info("Test for compute()...")
        matrix = Blosum62()
        msa = [('ID1',
                 '---'),
                ('ID2',
                 '---')]
        sumofpairs = SumOfPairs(matrix)

        result = sumofpairs.compute(msa)
        expected = 3
        self.assertEqual(expected, result)

    def test_get_score_of_A_and_G(self):
        logger.info("Test for get_score_of_two_chars()...")
        matrix = Blosum62()
        charA, charB = 'A', '-'
        sumofpairs = SumOfPairs(matrix)

        result = sumofpairs.get_score_of_two_chars(charA, charB)
        expected = -8
        self.assertEqual(expected, result)

    def test_get_score_of_column(self):
        logger.info("Test for get_score_of_k_column()...")
        matrix = Blosum62()
        column = ['-', '-', '-']
        sumofpairs = SumOfPairs(matrix)

        result = sumofpairs.get_score_of_k_column(column)
        expected = 3
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()