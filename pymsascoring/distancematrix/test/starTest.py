# -*- coding: utf-8 -*-
"""
Created on Sat Mar 18 16:02:34 2017

@author: Migue
"""
import unittest
from pymsascoring.impl.star import Star


class Test(unittest.TestCase):
    def setUp(self):
        print("setUp: INICIANDO TEST")

    def tearDown(self):
        print("tearDown: FINALIZANDO TEST")

    def test1(self):
        print("Test1")
        seqs = [('sec1', 'AA'), ('sec2', 'AC'),('sec3','AC')]
        final_score = Star.get_seqs_only(seqs)
        self.assertEqual(34, final_score)

    def test2(self):
        print("Test2")
        seqs = [('sec1', 'KKA'), ('sec2', 'A-A')]
        final_score = Star.sumStar(seqs)
        self.assertEqual(10, final_score)


if __name__ == "__main__":
    unittest.main()
