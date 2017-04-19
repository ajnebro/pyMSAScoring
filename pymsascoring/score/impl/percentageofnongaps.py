from pymsascoring.score.score import Score
import logging

__author__ = "Juan ignacio Álvarez"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "juaalvare@uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class PercentageOfNonGaps(Score):
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

    def percentage_of_non_gaps(self):
        """ Compute the percentage of non-gaps between sequences.

        :param msa: List of pairs -id and sequence- (i.e. "[('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]" ).
        :return: Percentage of non-gaps
        """

        t = 0  # Number of conserved columns
        sequences = self.get_seqs_from_list_of_pairs(self.msa)  # List of sequences
        tamVal = len(sequences[0])  # Lenght of the first sequence

        for value in sequences:
            for i in range(tamVal):
                t += value[i].count('-')

        logger.info('Total number of gaps: {0}'.format(t))
        logger.info('Total number of non-gaps: {0}'.format(tamVal*2 - t))
        return 100 - (t / (tamVal * len(sequences)) * 100)
