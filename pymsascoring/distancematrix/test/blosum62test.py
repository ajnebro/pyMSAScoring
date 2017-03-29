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