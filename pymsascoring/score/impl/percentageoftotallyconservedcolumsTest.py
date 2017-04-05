#Author: Juan Ignacio Álvarez

import unittest

from pymsascoring.score.impl.percentageofnongaps import PercentageOfNonGaps
from pymsascoring.score.impl.percentageoftotallyconservedcolumns import PercentageOfTotallyConservedColumns


class PercentageOfTotallyConservedColumnsTest(unittest.TestCase):
    def setUp(self):
        print("setUp: Initiating Test")

    def tearDown(self):
        print("tearDown: Finishing Test")

    def test_percentage_of_totally_conserved_columns(self):
        print("Executing Test1")
        a = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfTotallyConservedColumns(a)
        expected = 100
        result = self.per.percentage_of_totally_conserved_columns()
        self.assertEqual(result, expected)


    def test_percentage_of_non_gaps(self):
        print("Executing Test2")
        a = [["S1", "-----A-A-A"], ["S2", "----A-A--A"]]
        self.per = PercentageOfNonGaps(a)
        expected = 10
        result = self.per.percentage_of_non_gaps()
        self.assertEqual(result, expected)

    if __name__ == '__main__':
        unittest.main()
