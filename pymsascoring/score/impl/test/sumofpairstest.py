import unittest

from pymsascoring.distancematrix.impl.blosum62 import Blosum62
from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.score.impl import SumOfPairs

__author__  = "René Betancor"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__  = "Development"


class SumOfPairsTestCase(unittest.TestCase):

    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")

    def test_basic_score_of_12_with_PAM250(self):
        print("Ejecutando test1")
        matrix = PAM250()
        msa = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        final_score = SumOfPairs(matrix)
        self.assertEqual(12, final_score.compute(msa))

    def test_basic_score_of_12_with_BLOSUM62(self):
        print("Ejecutando test2")
        matrix = Blosum62()
        msa = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        final_score = SumOfPairs(matrix)
        self.assertEqual(24, final_score.compute(msa))

    def test_basic_score_with_gaps_BLOSUM62(self):
        print("Ejecutando test3")
        matrix = Blosum62()
        msa = [('ID1',
                 'FA'),
                ('ID2',
                 'A-')]
        final_score = SumOfPairs(matrix)
        self.assertEqual(-10, final_score.compute(msa))

    def test_only_gaps_with_BLOSUM62(self):
        print("Ejecutando test4")
        matrix = Blosum62()
        msa = [('ID1',
                 '---'),
                ('ID2',
                 '---')]
        final_score = SumOfPairs(matrix)
        self.assertEqual(3, final_score.compute(msa))


if __name__ == "__main__":
    unittest.main()