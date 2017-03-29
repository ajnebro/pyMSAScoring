import unittest

from pymsascoring.distancematrix.distancematrix import DistanceMatrix

__author__ = "Antonio J. Nebro"

class TestMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_should_default_gap_penalty_be_minus_eight(self):
        matrix = DistanceMatrix()

        self.assertEqual(-8, matrix.get_gap_penalty())

    def test_should_constructor__modify_the_gap_penalty(self):
        matrix = DistanceMatrix(-10)

        self.assertEqual(-10, matrix.get_gap_penalty())

    def test_should_get_distance_return_the_gap_penalty_if_a_char_is_a_gap(self):
        matrix = DistanceMatrix()

        self.assertEqual(matrix.get_gap_penalty(), matrix.get_distance('A', '-'))
        self.assertEqual(matrix.get_gap_penalty(), matrix.get_distance('-', 'B'))

    def test_should_get_distance_return_one_if_the_two_chars_are_gaps(self):
        matrix = DistanceMatrix()

        self.assertEqual(1, matrix.get_distance('-', '-'))

if __name__ == '__main__':
    unittest.main()