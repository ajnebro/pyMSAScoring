"""

Author: Guillermo López

"""

import unittest
from pymsascoring.impl.entropy import Entropy
#from entropy import Entropy


class EntropyTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")

    def test_should_entropy_of_two_seqs_return_0(self):
        print("Ejecutando test1")
        msa = [("S1", "AAAA"), ("S2", "AAAA")]
        self.ent = Entropy(msa)
        expected_value = 0
        recieved_value = self.ent.compute()
        self.assertEqual(expected_value, recieved_value)

    def test_should_entropy_of_four_seqs_return_minus_2_point_77(self):
        print("Ejecutando test2")
        msa = [("S1", "ACGT"), ("S2", "ACGT"), ("S3", "TGCA"), ("S4", "TGCA")]
        self.ent = Entropy(msa)
        expected_value = -2.77
        recieved_value = round(self.ent.compute(), 2)
        self.assertEqual(expected_value, recieved_value)

    def test_should_entropy_of_three_seqs_with_gaps_return_minus_6_point_94(self):
        print("Ejecutando test4")
        msa = [("S1", "A-TGCAAT-G"), ("S2", "-CT-CCAT-A"), ("S3", "-TTAT-CTG-")]
        self.ent = Entropy(msa)
        expected_value = -6.94
        recieved_value = round(self.ent.compute(), 2)
        self.assertEqual(expected_value, recieved_value)

if __name__ == "__main__":
    unittest.main()
