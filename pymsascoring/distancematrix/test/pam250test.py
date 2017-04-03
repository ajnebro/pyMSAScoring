"""
    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import unittest
from pymsascoring.distancematrix.impl.pam250 import PAM250

__author__ = "Antonio J. Nebro"

class TestMethods(unittest.TestCase):

    def setUp(self):
        pass

    def test_should_default_gap_penalty_be_minus_eight(self):
        matrix = PAM250()

        self.assertEqual(-8, matrix.get_gap_penalty())

    def test_should_constructor__modify_the_gap_penalty(self):
        matrix = PAM250(-10)

        self.assertEqual(-10, matrix.get_gap_penalty())

    def test_should_get_distance_return_the_gap_penalty_if_a_char_is_a_gap(self):
        matrix = PAM250()

        self.assertEqual(matrix.get_gap_penalty(), matrix.get_distance('A', '-'))
        self.assertEqual(matrix.get_gap_penalty(), matrix.get_distance('-', 'B'))

    def test_should_get_distance_return_one_if_the_two_chars_are_gaps(self):
        matrix = PAM250()

        self.assertEqual(1, matrix.get_distance('-', '-'))

    def test_should_get_distance_return_the_correct_values_if_there_are_no_gaps(self):
        matrix = PAM250()

        self.assertEqual(-2, matrix.get_distance('A', 'R'))
        self.assertEqual(-3, matrix.get_distance('N', 'F'))
        self.assertEqual(-3, matrix.get_distance('X', 'C'))
        self.assertEqual(+5, matrix.get_distance('I', 'I'))
        self.assertEqual(+4, matrix.get_distance('V', 'V'))

    def test_should_get_distance_throw_an_exception_if_a_char_is_invalid(self):
        matrix = PAM250()

        with self.assertRaises(Exception):
            matrix.get_distance('J', 'A')

if __name__ == '__main__':
    unittest.main()
