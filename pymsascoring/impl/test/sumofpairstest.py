import unittest
from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.distancematrix.impl.blosum62 import Blosum62
from pymsascoring.impl.sumofpairs import SumOfPairs


class TestMethods(unittest.TestCase):

    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")

    def test_basic_score_of_12_with_PAM250(self):
        print("Ejecutando test1")
        matrix = PAM250()
        seqs = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        final_score = SumOfPairs(seqs, matrix)
        self.assertEqual(12, final_score.calc_final_score())

    def test_basic_score_of_12_with_BLOSUM62(self):
        print("Ejecutando test2")
        matrix = Blosum62()
        seqs = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        final_score = SumOfPairs(seqs, matrix)
        self.assertEqual(24, final_score.calc_final_score())

    def test_basic_score_with_gaps_BLOSUM62(self):
        print("Ejecutando test3")
        matrix = Blosum62()
        seqs = [('ID1',
                 'FA'),
                ('ID2',
                 'A-')]
        final_score = SumOfPairs(seqs, matrix)
        self.assertEqual(-10, final_score.calc_final_score())

    def test_only_gaps_with_BLOSUM62(self):
        print("Ejecutando test4")
        matrix = Blosum62()
        seqs = [('ID1',
                 '---'),
                ('ID2',
                 '---')]
        final_score = SumOfPairs(seqs, matrix)
        self.assertEqual(3, final_score.calc_final_score())