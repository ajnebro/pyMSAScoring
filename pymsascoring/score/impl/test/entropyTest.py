import unittest
from pymsascoring.score.impl.entropy import Entropy

__author__ = "Guillermo López"
__copyright__ = ""
__credits__ = ["Guillermo López", "Pablo Rodríguez"]
__license__ = "GPL"
__version__ = "1.0"
__status__ = "Development"
__email__ = ["guilopgar@uma.es", "pabrod@uma.es"]


class EntropyTestCase(unittest.TestCase):
    def setUp(self):
        self.ent = Entropy()

    def test_get_entropy_of_a_column_with_gaps(self):
        d = {"-": 0.8, "A": 0.2}

        expected_value = -0.5
        received_value = round(self.ent.get_column_entropy(d), 1)

        self.assertEqual(expected_value, received_value)

    def test_get_entropy_of_a_gapped_column(self):
        d = {"-": 1}

        expected_value = 0
        received_value = self.ent.get_column_entropy(d)

        self.assertEqual(expected_value, received_value)

    def test_get_dictionary_of_a_five_letter_colum(self):
        msa = [("S1", "-"), ("S2", "A"), ("S3", "C"), ("S4", "G"), ("S5", "T")]
        col = 0
        tot_seqs = 5

        expected_value = {"-": 1 / tot_seqs, "A": 1 / tot_seqs, "C": 1 / tot_seqs, "G": 1 / tot_seqs, "T": 1 / tot_seqs}
        received_value = self.ent.get_dictionary(msa, col, tot_seqs)

        self.assertEqual(expected_value, received_value)

    def test_get_dictionary_of_a_gapped_colum(self):
        msa = [("S1", "A-"), ("S2", "--"), ("S3", "T-"), ("S4", "--")]
        col = 1
        tot_seqs = 4

        expected_value = {"-": 1}
        received_value = self.ent.get_dictionary(msa, col, tot_seqs)

        self.assertEqual(expected_value, received_value)

    def test_compute_of_four_seqs_with_no_gaps(self):
        msa = [("S1", "ACGT"), ("S2", "ACGT"), ("S3", "TGCA"), ("S4", "TGCA")]

        expected_value = -2.77
        received_value = round(self.ent.compute(msa), 2)

        self.assertEqual(expected_value, received_value)

    def test_compute_of_three_seqs_with_gaps(self):
        msa = [("S1", "A-TGCAAT-G"), ("S2", "-CT-CCAT-A"), ("S3", "-TTAT-CTG-")]

        expected_value = -6.94
        received_value = round(self.ent.compute(msa), 2)

        self.assertEqual(expected_value, received_value)

    def test_compute_of_two_gapped_seqs(self):
        msa = [("S1", "-----"), ("S2", "-----")]

        expected_value = 0
        received_value = self.ent.compute(msa)

        self.assertEqual(expected_value, received_value)


if __name__ == "__main__":
    unittest.main()
