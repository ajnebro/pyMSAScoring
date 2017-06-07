import logging
import unittest

from pymsascoring.score import SumOfPairs, Star, PercentageOfTotallyConservedColumns, Entropy
from pymsascoring.substitutionmatrix import PAM250, Blosum62

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SumOfPairsTestCases(unittest.TestCase):
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


class StarTestCases(unittest.TestCase):
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

class PercentageOfTotallyConservedColumnsTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_percentage_of_totally_conserved_columns_100(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_100()...")

        # setup
        msa = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfTotallyConservedColumns(msa)

        # results
        result = self.per.percentage_of_totally_conserved_columns()
        expected = 100

        # check
        self.assertEqual(result, expected)


class PercentageOfTotallyConservedColumnsTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_percentage_of_totally_conserved_columns_100(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_100()...")

        # setup
        msa = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfTotallyConservedColumns(msa)

        # results
        result = self.per.percentage_of_totally_conserved_columns()
        expected = 100

        # check
        self.assertEqual(result, expected)


class EntropyTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")
        self.ent = Entropy()

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_get_entropy_of_a_column_with_gaps(self):
        logger.info("Test for test_get_entropy_of_a_column_with_gaps()...")

        # setup
        d = {"-": 0.8, "A": 0.2}

        # results
        result = round(self.ent.get_column_entropy(d), 1)
        expected = -0.5

        # check
        self.assertEqual(expected, result)

    def test_get_entropy_of_a_gapped_column(self):
        logger.info("Test for test_get_entropy_of_a_gapped_column()...")

        # setup
        d = {"-": 1}

        # results
        expected = 0
        result = self.ent.get_column_entropy(d)

        # check
        self.assertEqual(expected, result)

    def test_get_dictionary_of_a_five_letter_column(self):
        logger.info("Test for test_get_dictionary_of_a_five_letter_column()...")

        # setup
        column = ("-", "A", "C", "G", "T")
        tot_seqs = len(column)

        # results
        expected = {"-": 1 / tot_seqs, "A": 1 / tot_seqs, "C": 1 / tot_seqs, "G": 1 / tot_seqs, "T": 1 / tot_seqs}
        result = self.ent.get_frecuencies(column)

        # check
        self.assertEqual(expected, result)

    def test_get_dictionary_of_a_gapped_column(self):
        logger.info("Test for test_get_dictionary_of_a_gapped_column()...")

        # setup
        column = ("-", "-", "-", "-", "-")

        # results
        expected = {"-": 1}
        result = self.ent.get_frecuencies(column)

        # check
        self.assertEqual(expected, result)

    def test_compute_of_four_seqs_with_no_gaps(self):
        logger.info("Test for test_compute_of_four_seqs_with_no_gaps()...")

        # setup
        msa = [("S1", "ACGT"), ("S2", "ACGT"), ("S3", "TGCA"), ("S4", "TGCA")]

        # results
        expected = -2.77
        result = round(self.ent.compute(msa), 2)

        # check
        self.assertEqual(expected, result)

    def test_compute_of_three_seqs_with_gaps(self):
        logger.info("Test for test_compute_of_three_seqs_with_gaps()...")

        # setup
        msa = [("S1", "A-TGCAAT-G"), ("S2", "-CT-CCAT-A"), ("S3", "-TTAT-CTG-")]

        # results
        expected = -6.94
        result = round(self.ent.compute(msa), 2)

        # check
        self.assertEqual(expected, result)

    def test_compute_of_two_gapped_seqs(self):
        logger.info("Test for test_compute_of_two_gapped_seqs()...")

        # setup
        msa = [("S1", "-----"), ("S2", "-----")]

        # results
        expected = 0
        result = self.ent.compute(msa)

        # check
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()