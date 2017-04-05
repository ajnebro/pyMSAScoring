from pymsascoring.score import Score
import itertools
import logging

__author__  = "Antonio Benítez, René Betancor"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__  = "Development"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class SumOfPairs(Score):
    """ Class for returning the alignment score of >1 sequences given the substituion matrix. """

    def __init__(self, DM):
        self.substitution_matrix = DM
        self.sequences = [] # list of sequences

    def get_seqs_from_list_of_pairs(self, msa):
        """ Get the second value of a list with multiple elements.

        :param msa: List of pairs -id and sequence- (i.e. "[('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]" ).
        :return: List of sequences (i.e. "('AB', 'CD', 'EF' )").
        """

        logger.debug('List of pairs: {0}'.format(msa))
        for i in range(len(msa)):
            self.sequences.append(msa[i][1])
        logger.debug('List of sequences: {0}'.format(self.sequences))
        return self.sequences

    def compute(self, msa):
        """ Compute the score of two or more sequences using the "Sum of Pairs" method.

        :param msa: List of pairs -id and sequence- (i.e. "[('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]" ).
        :return: List of sequences.
        """

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
            for charA, charB in itertools.combinations(column, 2):  # compare each element of the list 'column' with the others only one time
                partial_score = self.get_score(charA, charB)
                final_score += + partial_score
                logger.debug('Score of {0} and {1}: {2}'.format(charA, charB, partial_score))
            column.clear()  # clear the list for the next column

        logger.info('Final score: {0}'.format(final_score))
        return final_score

    def get_score(self, charA, charB):
        """ Return the score of two chars using the substituion matrix.

        :param charA: First char.
        :param charB: Second char.
        :return: Value of the score.
        """

        return int(self.substitution_matrix.get_distance(charA, charB))