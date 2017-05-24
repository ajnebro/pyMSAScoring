import unittest

from pymsascoring.score.impl.percentageoftotallyconservedcolumns import PercentageOfTotallyConservedColumns
from pymsascoring.score.impl.percentageofnongaps import PercentageOfNonGaps

__author__ = "Juan ignacio Álvarez"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "juaalvare@uma.es"


class PercentageOfTotallyConservedColumnsTest(unittest.TestCase):
    def setUp(self):
        print("setUp: Initiating Test")

    def tearDown(self):
        print("tearDown: Finishing Test")

    def test_percentage_of_totally_conserved_columns(self):
        print("Executing Test1")
        msa = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfTotallyConservedColumns(msa)
        expected = 100
        result = self.per.percentage_of_totally_conserved_columns()
        self.assertEqual(result, expected)

    def test_percentage_of_non_gaps(self):
        print("Executing Test2")
        msa = [["S1", "-----A-A-A"], ["S2", "----A-A--A"]]
        self.per = PercentageOfNonGaps(msa)
        expected = 10
        result = self.per.percentage_of_non_gaps()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
