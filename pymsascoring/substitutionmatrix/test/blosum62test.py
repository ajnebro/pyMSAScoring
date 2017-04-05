import unittest
from pymsascoring.substitutionmatrix.impl.blosum62 import Blosum62

__author__ = "Antonio J. Nebro"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "antonio@lcc.uma.es"

class TestMethods(unittest.TestCase):
    def setUp(self):
        pass

    def setUp(self):
        pass

    def test_should_default_gap_penalty_be_minus_eight(self):
        matrix = Blosum62()

        self.assertEqual(-8, matrix.get_gap_penalty())

    def test_should_constructor__modify_the_gap_penalty(self):
        matrix = Blosum62(-10)

        self.assertEqual(-10, matrix.get_gap_penalty())

    def test_should_get_distance_return_the_gap_penalty_if_a_char_is_a_gap(self):
        matrix = Blosum62()

        self.assertEqual(matrix.get_gap_penalty(), matrix.get_distance('A', '-'))
        self.assertEqual(matrix.get_gap_penalty(), matrix.get_distance('-', 'B'))

    def test_should_get_distance_return_one_if_the_two_chars_are_gaps(self):
        matrix = Blosum62()

        self.assertEqual(1, matrix.get_distance('-', '-'))

    def test_should_get_distance_return_the_correct_values_if_there_are_no_gaps(self):
        matrix = Blosum62()

        self.assertEqual(-1, matrix.get_distance('A', 'R'))
        self.assertEqual(-3, matrix.get_distance('N', 'F'))
        self.assertEqual(-2, matrix.get_distance('X', 'C'))
        self.assertEqual(+4, matrix.get_distance('I', 'I'))
        self.assertEqual(+4, matrix.get_distance('V', 'V'))

    def test_should_get_distance_throw_an_exception_if_a_char_is_invalid(self):
        matrix = Blosum62()

        with self.assertRaises(Exception):
            matrix.get_distance('J', 'A')

if __name__ == '__main__':
    unittest.main()

