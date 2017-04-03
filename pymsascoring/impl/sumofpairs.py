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


from pymsascoring.score import Score
import itertools
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


__author__ = 'Antonio Benítez, René Betancor'


class SumOfPairs(Score):
    """
    Class for returning the alignment score of >1 sequences given the substituion matrix..

    get_seq_only        Get the second value of a list with multiple elements.
    calc_score          Given two char, return the partial score.
    calc_final_socre    Get the final score of the alignment.
    """

    def __init__(self, substitution_matrix):
        self.substitution_matrix = substitution_matrix
        self.sequences = [] # list of sequences

    def get_seqs_from_list_of_pairs(self, msa):
        logger.debug('List of pairs: {0}'.format(msa))
        for i in range(len(msa)):  # list_of_pairs = [('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]
            self.sequences.append(msa[i][1])  # sequences = ('AB', 'CD', 'EF' )
        logger.debug('List of sequences: {0}'.format(self.sequences))
        return self.sequences

    def compute(self, msa):
        logger.info('Computing score...')
        sequences = self.get_seqs_from_list_of_pairs(msa)
        tamSeq = len(sequences[0])  # length of the first sequence (= length to the second one, third one...)
        logger.debug('Lengh of a sequence: {0}'.format(tamSeq))
        column = []
        final_score = 0

        for k in range(tamSeq):
            for sequence in sequences:
                column.append(sequence[k])  # add to 'column' the k-char of each sequence
            logger.debug('{0}-column: {1}'.format(k, column))
            #print(column)  # column = ['A', 'C', 'E'] (the first time), ['-', 'D', '-'] (the second)
            for charA, charB in itertools.combinations(column, 2):  # compare each element of the list 'column' with the others only one time
                partial_score = self.get_score(charA, charB)
                final_score += + partial_score
                logger.debug('Score of {0} and {1}: {2}'.format(charA, charB, partial_score))
            column.clear()  # clear the list for the next column

        logger.info('Final score: {0}'.format(final_score))
        return final_score

    def get_score(self, charA, charB):
        return int(self.substitution_matrix.get_distance(charA, charB))