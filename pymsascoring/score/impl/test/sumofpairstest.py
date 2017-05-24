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
        print("setUp: RUNNING TEST")
        self.sumofpairs_PAM250 = SumOfPairs(PAM250())
        self.sumofpairs_Blosum62 = SumOfPairs(Blosum62())

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_basic_score_of_12_with_PAM250(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', 'AA'), ('ID2', 'AA'), ('ID3', 'AA')]

        # results
        result = self.sumofpairs_PAM250.compute(msa)
        expected = 12

        # check
        self.assertEqual(expected, result)

    def test_basic_score_of_12_with_BLOSUM62(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', 'AA'), ('ID2', 'AA'), ('ID3', 'AA')]

        # results
        result = self.sumofpairs_Blosum62.compute(msa)
        expected = 24

        # check
        self.assertEqual(expected, result)

    def test_basic_score_with_gaps_BLOSUM62(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', 'FA'), ('ID2', 'A-')]

        # results
        result = self.sumofpairs_Blosum62.compute(msa)
        expected = -10

        # check
        self.assertEqual(expected, result)

    def test_only_gaps_with_BLOSUM62(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', '---'), ('ID2', '---')]

        # results
        result = self.sumofpairs_Blosum62.compute(msa)
        expected = 3

        # check
        self.assertEqual(expected, result)

    def test_get_score_of_A_and_gap(self):
        logger.info("Test for get_score_of_two_chars()...")

        # setup
        charA, charB = 'A', '-'

        # results
        result = self.sumofpairs_Blosum62.get_score_of_two_chars(charA, charB)
        expected = -8

        # check
        self.assertEqual(expected, result)

    def test_get_score_of_column_with_only_gaps(self):
        logger.info("Test for get_score_of_k_column()...")

        # setup
        column = ['-', '-', '-']

        # results
        result = self.sumofpairs_Blosum62.get_score_of_k_column(column)
        expected = 3

        # check
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()