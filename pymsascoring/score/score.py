import logging

__author__ = "Antonio J. Nebro"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "antonio@lcc.uma.es"

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Score:
    """ Class representing MSA (Multiple Sequence Alignment) scores
    
    A msa has to be a Python list containing pairs of (identifier, sequence), as in this example:
    ((id1, SSSBA), (id2, HHALK), (id3, -HLGS), etc))
    
    Requirements:
    - All the sequences in an msa must be aligned
    - The gap character is '-'
    
    """
    def compute(self, msa) -> float:
        """ Compute the score 
        
        :param msa
        :return: the value of the score
        """
        pass

    def get_seqs_from_list_of_pairs(self, msa):
        """ Get the sequences from an msa.

        :param msa: Python list containing pairs of (identifier, sequence)
        :return: List of sequences (i.e. "('AB', 'CD', 'EF' )") if all sequences are of the same length.
        """

        sequences = []

        logger.debug('List of pairs: {0}'.format(msa))
        for i in range(len(msa)):
            sequences.append(msa[i][1])
        logger.debug('List of sequences: {0}'.format(sequences))

        return sequences \
            if all(len(sequences[0]) == len(seq) for seq in sequences) \
            else self._raiser('Sequences are not of the same length.')

    def _raiser(self, e): raise Exception(e)