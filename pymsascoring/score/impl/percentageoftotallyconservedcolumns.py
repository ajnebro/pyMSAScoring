from pymsascoring.score.score import Score
import logging

__author__ = "Juan ignacio Álvarez"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "juaalvare@uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PercentageOfTotallyConservedColumns(Score):
    def __init__(self, msa):
        self.msa = msa

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

    def percentage_of_totally_conserved_columns(self):
        sequences = self.get_seqs_from_list_of_pairs(self.msa)  # List of sequences
        length_sequence = len(sequences[0])

        column = []
        percentage = 0

        for k in range(length_sequence):
            for value in sequences:
                column.append(value[k])
            if len(set(column)) <= 1:
                percentage += 1
            column.clear()

        logger.info('Total number of conserved colums: {0} out of {1}'.format(percentage, length_sequence))
        return percentage / length_sequence * 100