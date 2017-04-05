
import unittest
<<<<<<< HEAD

from pymsascoring.score.impl.star import Star
=======
from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.distancematrix.impl.blosum62 import Blosum62
from pymsascoring.impl.star import Star
>>>>>>> fc8b3de7b0f4f5672892f3a397b5ca8815a167a4

__author__ = "Miguel Angel, Daniel Torres Ramírez"
__license__ = "GNU"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "miggalrui@uma.es"



class Test(unittest.TestCase):

    def setUp(self):
        print("setUp: STARTING TEST")

    def tearDown(self):
        print("tearDown: ENDING TEST")

    # Test for a Blosum62 with 3 strings of 2 characters, comparing with the valid result
    def test1(self):
        print("Test1")
        matrix = Blosum62()
        seqs = [('sec1','AA'),('sec2','AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(30, final_score.sumStar())

    #  Test for a Blosum62 with 3 strings of 2 characters, comparing with the incorrect result
    def test2(self):
        print("Test2")
        matrix = Blosum62()
        seqs = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        with self.assertRaises(Exception):
            self.assertEqual(22, final_score.sumStar())

    # Test for a PAM250 with 3 strings of 2 characters, comparing with the invalid result
    def test3(self):
        print("Test3")
        matrix = PAM250()
        seqs = [('sec1','AA'),('sec2','AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(28, final_score.sumStar())

    # Test for a pam250 with 3 strings of 2 characters, comparing with the invalid result
    def test4(self):
        print("Test4")
        matrix = PAM250()
        seqs = [('sec1','AA'),('sec2','AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        with self.assertRaises(Exception):
            self.assertEqual(22, final_score.sumStar())

    # Test for a PAM250 with 3 strings of 2 characters and a GAP, comparing with the valid result
    def test5(self):
        print("Test5")
        matrix = PAM250()
        seqs = [('sec1','AA'),('sec2','A-'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(-2, final_score.sumStar())

    # Test for a Blosum62 with 3 strings of 2 characters and a GAP, comparing with the valid result
    def test6(self):
        print("Test6")
        matrix = Blosum62()
        seqs = [('sec1','AA'),('sec2','A-'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(8, final_score.sumStar())

if __name__ == "__main__":
    unittest.main()
