import unittest
import logging
from pymsascoring.score.impl.entropy import Entropy

__author__ = "Guillermo López"
__copyright__ = ""
__credits__ = ["Guillermo López", "Pablo Rodríguez"]
__license__ = "GPL"
__version__ = "1.0"
__status__ = "Development"
__email__ = ["guilopgar@uma.es", "pabrod@uma.es"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class EntropyTestCase(unittest.TestCase):
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
        column = ("-","A","C","G","T")
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
