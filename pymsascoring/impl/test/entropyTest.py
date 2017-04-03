import unittest
from pymsascoring.impl.entropy import Entropy

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

    def test_should_compute_of_two_seqs_return_0(self):
        msa = [("S1", "AAAA"), ("S2", "AAAA")]
        self.ent = Entropy()
        expected_value = 0
        recieved_value = self.ent.compute(msa)
        self.assertEqual(expected_value, recieved_value)

    def test_should_compute_of_four_seqs_return_minus_2_point_77(self):
        msa = [("S1", "ACGT"), ("S2", "ACGT"), ("S3", "TGCA"), ("S4", "TGCA")]
        self.ent = Entropy()
        expected_value = -2.77
        recieved_value = round(self.ent.compute(msa), 2)
        self.assertEqual(expected_value, recieved_value)

    def test_should_compute_of_three_seqs_with_gaps_return_minus_6_point_94(self):
        msa = [("S1", "A-TGCAAT-G"), ("S2", "-CT-CCAT-A"), ("S3", "-TTAT-CTG-")]
        self.ent = Entropy()
        expected_value = -6.94
        recieved_value = round(self.ent.compute(msa), 2)
        self.assertEqual(expected_value, recieved_value)

if __name__ == "__main__":
    unittest.main()
