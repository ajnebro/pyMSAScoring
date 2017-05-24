import unittest
import logging
from pymsascoring.score.impl.percentageoftotallyconservedcolumns import PercentageOfTotallyConservedColumns

__author__ = "Juan ignacio Álvarez"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "juaalvare@uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PercentageOfTotallyConservedColumnsTest(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_percentage_of_totally_conserved_columns_100(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_100()...")

        # setup
        msa = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfTotallyConservedColumns(msa)

        # results
        result = self.per.percentage_of_totally_conserved_columns()
        expected = 100

        # check
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
