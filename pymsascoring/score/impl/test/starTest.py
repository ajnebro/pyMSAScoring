import unittest
import logging
from pymsascoring.substitutionmatrix.impl.pam250 import PAM250
from pymsascoring.substitutionmatrix.impl.blosum62 import Blosum62
from pymsascoring.score.impl.star import Star

__author__ = "Miguel Angel, Daniel Torres Ramírez"
__license__ = "GNU"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "miggalrui@uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class StarTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")
        self.star_PAM250 = Star(PAM250())
        self.star_Blosum62 = Star(Blosum62())

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_most_frequent_A_with_BLOSUM62(self):
        logger.info("Test for test_most_frequent_with_BLOSUM62()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_Blosum62.compute(msa)
        expected = 30

        # check
        self.assertEqual(expected, result)

    def test_most_frequent_error_with_BLOSUM62(self):
        logger.info("Test for test_most_frequent_error_with_BLOSUM62()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_Blosum62.compute(msa)
        expected = 22

        # check
        with self.assertRaises(Exception):
            self.assertEqual(expected, result)

    def test_most_frequent_with_PAM250(self):
        logger.info("Test for test_most_frequent_with_PAM250()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_PAM250.compute(msa)
        expected = 28

        # check
        self.assertEqual(expected, result)

    def test_most_frequent_error_with_PAM250(self):
        logger.info("Test for test_most_frequent_error_with_PAM250()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_PAM250.compute(msa)
        expected = 22

        # check
        with self.assertRaises(Exception):
            self.assertEqual(expected, result)

    def test_most_frequent_gaps_with_PAM250(self):
        logger.info("Test for test_most_frequent_gaps_with_PAM250()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'A-'), ('sec3', 'AC')]

        # results
        result = self.star_PAM250.compute(msa)
        expected = -2

        # check
        self.assertEqual(expected, result)

    def test_most_frequent_gaps_with_BLOSUM62(self):
        logger.info("Test for test_most_frequent_gaps_with_BLOSUM62()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'A-'), ('sec3', 'AC')]

        # results
        result = self.star_Blosum62.compute(msa)
        expected = 8

        # check
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
