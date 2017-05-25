from pymsascoring.score.score import Score
from collections import Counter
import logging

__author__ = "Daniel Torres Ramírez,Miguel Angel"
__license__ = "GNU"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "dantorram@uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Star(Score):
    def __init__(self, substitution_matrix):
        self.substitution_matrix = substitution_matrix

    def compute(self, msa):
        logger.debug('Computing score...')
        sequences = self.get_seqs_from_list_of_pairs(msa)
        length_sequence = len(sequences[0])  # length of the first sequence (= length to the second one, third one...)
        logger.debug('Lengh of a sequence: {0}'.format(length_sequence))

        column = []
        final_score = 0

        for k in range(length_sequence):
            for sequence in sequences:
                column.append(sequence[k])  # add to 'column' the k-char of each sequence
            logger.debug('{0}-column: {1}'.format(k, column))
            final_score += self.get_score_of_k_column(column)
            column.clear()  # clear the list for the next column

        return final_score

    def get_score_of_k_column(self, column):
        """ Compare the most frequent element of the list 'column' with the others only one time.

        :param column: List of chars.
        :return: Score of two chars.
        """

        score_of_column = 0
        most_frequent_char = Counter(column).most_common(1)[0][0]

        for char in column:
            score_of_column += self.get_score_of_two_chars(most_frequent_char, char)
            logger.debug('[-] Score of {0} and {1}: {2}'.format(most_frequent_char, char, self.get_score_of_two_chars(most_frequent_char, char)))

        logger.debug('[-] Score of column: {0}'.format(score_of_column))

        return score_of_column

    def get_score_of_two_chars(self, charA, charB):
        """ Return the score of two chars using the substituion matrix.

        :param charA: First char.
        :param charB: Second char.
        :return: Value of the score.
        """

        return int(self.substitution_matrix.get_distance(charA, charB))

