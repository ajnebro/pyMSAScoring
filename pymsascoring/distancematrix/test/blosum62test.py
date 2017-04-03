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

__author__ = "Antonio J. Nebro"

class TestMethods(unittest.TestCase):

    def setUp(self):
        pass


if __name__ == '__main__':
    unittest.main()


"""


  @Test
  public void shouldDefaultGapPenaltyValueBe8() {
    matrix = new Blosum62() ;
    assertEquals(-8, matrix.getGapPenalty());
  }

  @Test
  public void shouldConstructorWithPenalyValueModifyTheGapPenalty() {
    matrix = new Blosum62(-4) ;

    assertEquals(-4, matrix.getGapPenalty());
  }


  @Test
  public void shouldGetDistanceReturnTheGapPenaltyIfACharIsAGap() {
    matrix = new Blosum62() ;

    assertEquals(1, matrix.getDistance('-', '-'));
    assertEquals(matrix.getGapPenalty(), matrix.getDistance('A', '-'));
    assertEquals(matrix.getGapPenalty(), matrix.getDistance('-', 'A'));
  }

  @Test
  public void shouldGetDistanceReturnOneIfTheeCharsAreAGap() {
    matrix = new Blosum62() ;

    assertEquals(1, matrix.getDistance('-', '-'));
  }

  @Test
  public void shouldGetDistanceReturnTheCorrectValueIfTheCharsAreNotGaps() {
    matrix = new Blosum62() ;

    assertEquals(-1, matrix.getDistance('A', 'R'));
    assertEquals(-3, matrix.getDistance('N', 'F'));
    assertEquals(-2, matrix.getDistance('X', 'C'));
    assertEquals(+4, matrix.getDistance('I', 'I'));
    assertEquals(+4, matrix.getDistance('V', 'V'));
  }

  @Test(expected = JMetalException.class)
  public void shouldGetDistanceThrowAnExceptionIfACharIsInvalid() {
    matrix = new Blosum62() ;

    matrix.getDistance('J', 'A') ;
  }
"""