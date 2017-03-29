import unittest
from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.impl.sumofpairs import SumOfPairs


class TestMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_basic_score(self):
        matrix = PAM250()
        seqs = [('ID1',
                 'AA'),
                ('ID2',
                 'AA'),
                ('ID3',
                 'AA')]
        final_score = SumOfPairs(seqs, matrix)

        self.assertEqual(12, final_score.calc_final_score())

