import unittest
import entropy

class entropyTestCase(unittest.TestCase):
    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")

    def test_should_entropy_of_two_seqs_return_0(self):
        print("Ejecutando test1")
        msa = [("S1", "AAAA"), ("S2", "AAAA")]
        self.ent = entropy.Entropy(msa)
        expected_value = 0
        recieved_value = self.ent.calculate_minimum_entropy()
        self.assertEqual(expected_value, recieved_value)

    def test_should_entropy_of_four_seqs_return_minus_2_point_77(self):
        print("Ejecutando test2")
        msa = [("S1", "ACGT"), ("S2", "ACGT"), ("S3", "TGCA"), ("S4", "TGCA")]
        self.ent = entropy.Entropy(msa)
        expected_value = -2.77
        recieved_value = round(self.ent.calculate_minimum_entropy(), 2)
        self.assertEqual(expected_value, recieved_value)

    def test_should_entropy_of_three_seqs_return_minus_3_point_3(self):
        print("Ejecutando test3")
        msa = [("S1", "AAA"), ("S2", "CCC"), ("S3", "TTT")]
        self.ent = entropy.Entropy(msa)
        expected_value = -3.3
        recieved_value = round(self.ent.calculate_minimum_entropy(), 1)
        self.assertEqual(expected_value, recieved_value)

    def test_msas_illegal_lengths(self):
        print("Ejecutando test2")
        self.msas = multipleSequenceAlignmentScoring.MultipleSequenceAlignmentScoring("test1Fail.txt")
        with self.assertRaises(Exception):
            self.msas.percentage_of_totally_conserved_columns()



    def test_should_msas_cols_of_test1_file_return_3(self):
        print("Ejecutando test4")
        self.msas = multipleSequenceAlignmentScoring.MultipleSequenceAlignmentScoring("test.txt")
        expected_value = 3.03
        recieved_value = round(self.msas.percentage_of_totally_conserved_columns(), 2)
        self.assertEqual(expected_value, recieved_value)

    def test_should_msas_gaps_of_test1_file_return_87(self):
        print("Ejecutando test5")
        self.msas = multipleSequenceAlignmentScoring.MultipleSequenceAlignmentScoring("test.txt")
        expected_value = 87.12
        recieved_value = round(self.msas.percentage_of_non_gaps(), 2)
        self.assertEqual(expected_value, recieved_value)

if __name__ == "__main__":
    unittest.main()