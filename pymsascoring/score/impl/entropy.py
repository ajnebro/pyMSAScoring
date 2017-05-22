from pymsascoring.score.score import Score
import math
import logging

__author__ = "Pablo Rodríguez"
__copyright__ = ""
__credits__ = ["Pablo Rodríguez", "Guillermo López"]
__license__ = "GPL"
__version__ = "1.0"
__status__ = "Development"
__email__ = ["pabrod@uma.es", "guilopgar@uma.es"]

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Entropy(Score):

    def __init__(self):
        pass

    def get_seqs_from_list_of_pairs(self, msa):
        """ Get the second value of a list with multiple elements.

        :param msa: List of pairs -id and sequence- (i.e. "[('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]" ).
        :return: List of sequences (i.e. "('AB', 'CD', 'EF' )").
        """

        sequences = []

        logger.debug('List of pairs: {0}'.format(msa))
        for i in range(len(msa)):
            sequences.append(msa[i][1])
        logger.debug('List of sequences: {0}'.format(sequences))
        return sequences

    def compute(self, msa):
        """Compute minimum entropy for a MSA

        This function redefines the inherited function from Score (Parent Class).
        From multiple alignment sequences, it calculates the score of the column similarity
        using the Minimum Entropy formula.

        :param msa: MSA list of tuples
        :return score: Total score of MSA after calculating Minimum Entropy for each column
        """

        logger.info('Computing score...')
        sequences = self.get_seqs_from_list_of_pairs(msa)
        length_sequence = len(sequences[0])  # length of the first sequence (= length to the second one, third one...)
        logger.debug('Lengh of a sequence: {0}'.format(length_sequence))

        column = []
        final_score = 0

        for k in range(length_sequence):  # for every column of the sequences
            for sequence in sequences:
                column.append(sequence[k])  # add to list 'column' the k-char of each sequence
            char_and_frecuency = self.get_frecuencies(column)  # get the frecuency of each character
            final_score += self.get_column_entropy(char_and_frecuency)  # get the entropy of the column
            column.clear()  # clear the list for the next column

        return final_score

    def get_frecuencies(self, column):
        """Get dictionary of characters for the sequences list at current position

        :param column: list of characters of k-column

        :return dict: Dictionary in which the keys are characters and the
                value is the frequency that the key appears on the current column
        """

        dict = {}

        for character in set(column):
            dict[character] = column.count(character)/len(column)

        logger.debug('[-] Dict: {0}'.format(dict))
        return dict

    def get_column_entropy(self, dict):
        """Calculates the Minimum Entropy for the current column dictionary

        :param dict: Dictionary in which the keys are characters and the
               value is the frequency that key appears on the current column

        :return current_entropy: Minimum Entropy score of the current column
        """

        current_entropy = 0

        for key, value in dict.items():
            current_entropy += value * math.log(value)
            logger.debug('[-] Character {0}, frecuency: {1}, Entropy: {2})'.format(key, value, value * math.log(value)))

        return current_entropy
