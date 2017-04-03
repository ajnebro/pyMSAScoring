# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:02:34 2017

@author: Migue
"""
import unittest
from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.distancematrix.impl.blosum62 import Blosum62
from pymsascoring.impl.star import Star


class Test(unittest.TestCase):

    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")
        
    def test1(self):
        print("Test1")
        matrix = Blosum62()
        seqs = [('sec1','AA'),('sec2','AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(30, final_score.sumStar())

    def test2(self):
        print("Test2")
        matrix = Blosum62()
        seqs = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        with self.assertRaises(Exception):
            self.assertEqual(22, final_score.sumStar())

    def test3(self):
        print("Test3")
        matrix = PAM250()
        seqs = [('sec1','AA'),('sec2','AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(28, final_score.sumStar())

    def test4(self):
        print("Test4")
        matrix = PAM250()
        seqs = [('sec1','AA'),('sec2','AC'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        with self.assertRaises(Exception):
            self.assertEqual(22, final_score.sumStar())

    def test5(self):
        print("Test5")
        matrix = PAM250()
        seqs = [('sec1','AA'),('sec2','A-'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(-2, final_score.sumStar())

    def test6(self):
        print("Test6")
        matrix = Blosum62()
        seqs = [('sec1','AA'),('sec2','A-'), ('sec3', 'AC')]
        final_score = Star(seqs, matrix)
        self.assertEqual(8, final_score.sumStar())

if __name__ == "__main__":
    unittest.main()
