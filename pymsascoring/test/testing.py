import itertools
import logging
import math
import unittest

from collections import Counter

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class SubstitutionMatrix:
    """ Class representing a substitution matrix, such as PAM250, Blosum62, etc.

    Requirements:
    - The gap character is '-'
    """

    def __init__(self, gap_penalty=-8):
        self.gap_penalty = gap_penalty

    def get_distance(self, char1, char2):
        """ Returns the distance between two symbols

        :param char1:
        :param char2:
        :return: the distance value
        """
        if char1 is '-' and char2 is '-':
            result = 1
        elif char1 is '-' or char2 is '-':
            result = self.gap_penalty
        else:
            matrix = self.get_distance_matrix()
            if (char1, char2) in matrix:
                v = matrix[(char1, char2)]
            else:
                v = matrix[(char2, char1)]

            result = v

        return result


class PAM250(SubstitutionMatrix):
    """ Class implementing the PAM250 substitution matrix

    Reference: https://en.wikipedia.org/wiki/Point_accepted_mutation
    """

    def __init__(self, gap_penalty=-8):
        super(PAM250, self).__init__(gap_penalty)
        self.distance_matrix = \
            {('W', 'F'): 0, ('L', 'R'): -3, ('S', 'P'): 1, ('V', 'T'): 0, ('Q', 'Q'): 4, ('N', 'A'): 0, ('Z', 'Y'): -4,
             ('W', 'R'): 2, ('Q', 'A'): 0, ('S', 'D'): 0, ('H', 'H'): 6, ('S', 'H'): -1, ('H', 'D'): 1, ('L', 'N'): -3,
             ('W', 'A'): -6, ('Y', 'M'): -2, ('G', 'R'): -3, ('Y', 'I'): -1, ('Y', 'E'): -4, ('B', 'Y'): -3,
             ('Y', 'A'): -3,
             ('V', 'D'): -2, ('B', 'S'): 0, ('Y', 'Y'): 10, ('G', 'N'): 0, ('E', 'C'): -5, ('Y', 'Q'): -4,
             ('Z', 'Z'): 3,
             ('V', 'A'): 0, ('C', 'C'): 12, ('M', 'R'): 0, ('V', 'E'): -2, ('T', 'N'): 0, ('P', 'P'): 6, ('V', 'I'): 4,
             ('V', 'S'): -1, ('Z', 'P'): 0, ('V', 'M'): 2, ('T', 'F'): -3, ('V', 'Q'): -2, ('K', 'K'): 5,
             ('P', 'D'): -1,
             ('I', 'H'): -2, ('I', 'D'): -2, ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
             ('P', 'H'): 0,
             ('F', 'Q'): -5, ('Z', 'G'): 0, ('X', 'L'): -1, ('T', 'M'): -1, ('Z', 'C'): -5, ('X', 'H'): -1,
             ('D', 'R'): -1,
             ('B', 'W'): -5, ('X', 'D'): -1, ('Z', 'K'): 0, ('F', 'A'): -3, ('Z', 'W'): -6, ('F', 'E'): -5,
             ('D', 'N'): 2,
             ('B', 'K'): 1, ('X', 'X'): -1, ('F', 'I'): 1, ('B', 'G'): 0, ('X', 'T'): 0, ('F', 'M'): 0, ('B', 'C'): -4,
             ('Z', 'I'): -2, ('Z', 'V'): -2, ('S', 'S'): 2, ('L', 'Q'): -2, ('W', 'E'): -7, ('Q', 'R'): 1,
             ('N', 'N'): 2,
             ('W', 'M'): -4, ('Q', 'C'): -5, ('W', 'I'): -5, ('S', 'C'): 0, ('L', 'A'): -2, ('S', 'G'): 1,
             ('L', 'E'): -3,
             ('W', 'Q'): -5, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 1, ('N', 'R'): 0, ('H', 'C'): -3,
             ('Y', 'N'): -2,
             ('G', 'Q'): -1, ('Y', 'F'): 7, ('C', 'A'): -2, ('V', 'L'): 2, ('G', 'E'): 0, ('G', 'A'): 1, ('K', 'R'): 3,
             ('E', 'D'): 3, ('Y', 'R'): -4, ('M', 'Q'): -1, ('T', 'I'): 0, ('C', 'D'): -5, ('V', 'F'): -1,
             ('T', 'A'): 1,
             ('T', 'P'): 0, ('B', 'P'): -1, ('T', 'E'): 0, ('V', 'N'): -2, ('P', 'G'): 0, ('M', 'A'): -1, ('K', 'H'): 0,
             ('V', 'R'): -2, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -3, ('V', 'V'): 4, ('M', 'I'): 2,
             ('T', 'Q'): -1,
             ('I', 'G'): -3, ('P', 'K'): -1, ('M', 'M'): 6, ('K', 'D'): 0, ('I', 'C'): -2, ('Z', 'D'): 3,
             ('F', 'R'): -4,
             ('X', 'K'): -1, ('Q', 'D'): 2, ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -3, ('Z', 'H'): 2,
             ('B', 'L'): -3,
             ('B', 'H'): 1, ('F', 'F'): 9, ('X', 'W'): -4, ('B', 'D'): 3, ('D', 'A'): 0, ('S', 'L'): -3, ('X', 'S'): 0,
             ('F', 'N'): -3, ('S', 'R'): 0, ('W', 'D'): -7, ('V', 'Y'): -2, ('W', 'L'): -2, ('H', 'R'): 2,
             ('W', 'H'): -3,
             ('H', 'N'): 2, ('W', 'T'): -5, ('T', 'T'): 3, ('S', 'F'): -3, ('W', 'P'): -6, ('L', 'D'): -4,
             ('B', 'I'): -2,
             ('L', 'H'): -2, ('S', 'N'): 1, ('B', 'T'): 0, ('L', 'L'): 6, ('Y', 'K'): -4, ('E', 'Q'): 2, ('Y', 'G'): -5,
             ('Z', 'S'): 0, ('Y', 'C'): 0, ('G', 'D'): 1, ('B', 'V'): -2, ('E', 'A'): 0, ('Y', 'W'): 0, ('E', 'E'): 4,
             ('Y', 'S'): -3, ('C', 'N'): -4, ('V', 'C'): -2, ('T', 'H'): -1, ('P', 'R'): 0, ('V', 'G'): -1,
             ('T', 'L'): -2,
             ('V', 'K'): -2, ('K', 'Q'): 1, ('R', 'A'): -2, ('I', 'R'): -2, ('T', 'D'): 0, ('P', 'F'): -5,
             ('I', 'N'): -2,
             ('K', 'I'): -2, ('M', 'D'): -3, ('V', 'W'): -6, ('W', 'W'): 17, ('M', 'H'): -2, ('P', 'N'): 0,
             ('K', 'A'): -1,
             ('M', 'L'): 4, ('K', 'E'): 0, ('Z', 'E'): 3, ('X', 'N'): 0, ('Z', 'A'): 0, ('Z', 'M'): -2, ('X', 'F'): -2,
             ('K', 'C'): -5, ('B', 'Q'): 1, ('X', 'B'): -1, ('B', 'M'): -2, ('F', 'C'): -4, ('Z', 'Q'): 3,
             ('X', 'Z'): -1,
             ('F', 'G'): -5, ('B', 'E'): 3, ('X', 'V'): -1, ('F', 'K'): -5, ('B', 'A'): 0, ('X', 'R'): -1,
             ('D', 'D'): 4,
             ('W', 'G'): -7, ('Z', 'F'): -5, ('S', 'Q'): -1, ('W', 'C'): -8, ('W', 'K'): -3, ('H', 'Q'): 3,
             ('L', 'C'): -6,
             ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4, ('W', 'S'): -2, ('S', 'E'): 0, ('H', 'E'): 1,
             ('S', 'I'): -1,
             ('H', 'A'): -1, ('S', 'M'): -2, ('Y', 'L'): -1, ('Y', 'H'): 0, ('Y', 'D'): -4, ('E', 'R'): -1,
             ('X', 'P'): -1,
             ('G', 'G'): 5, ('G', 'C'): -3, ('E', 'N'): 1, ('Y', 'T'): -3, ('Y', 'P'): -5, ('T', 'K'): 0, ('A', 'A'): 2,
             ('P', 'Q'): 0, ('T', 'C'): -2, ('V', 'H'): -2, ('T', 'G'): 0, ('I', 'Q'): -2, ('Z', 'T'): -1,
             ('C', 'R'): -4,
             ('V', 'P'): -1, ('P', 'E'): -1, ('M', 'C'): -5, ('K', 'N'): 1, ('I', 'I'): 5, ('P', 'A'): 1,
             ('M', 'G'): -3,
             ('T', 'S'): 1, ('I', 'E'): -2, ('P', 'M'): -2, ('M', 'K'): 0, ('I', 'A'): -1, ('P', 'I'): -2,
             ('R', 'R'): 6,
             ('X', 'M'): -1, ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 2, ('X', 'E'): -1, ('Z', 'N'): 1, ('X', 'A'): 0,
             ('B', 'R'): -1, ('B', 'N'): 2, ('F', 'D'): -6, ('X', 'Y'): -2, ('Z', 'R'): 0, ('F', 'H'): -2,
             ('B', 'F'): -4,
             ('F', 'L'): 2, ('X', 'Q'): -1, ('B', 'B'): 3}

    def get_distance_matrix(self):
        return self.distance_matrix


class Blosum62(SubstitutionMatrix):
    """ Class implementing the Blosum62 substitution matrix

    Reference: https://en.wikipedia.org/wiki/BLOSUM
    """

    def __init__(self, gap_penalty=-8):
        super(Blosum62, self).__init__(gap_penalty)
        self.distance_matrix = \
            {('W', 'F'): 1, ('L', 'R'): -2, ('S', 'P'): -1, ('V', 'T'): 0, ('Q', 'Q'): 5, ('N', 'A'): -2,
             ('Z', 'Y'): -2,
             ('W', 'R'): -3, ('Q', 'A'): -1, ('S', 'D'): 0, ('H', 'H'): 8, ('S', 'H'): -1, ('H', 'D'): -1,
             ('L', 'N'): -3,
             ('W', 'A'): -3, ('Y', 'M'): -1, ('G', 'R'): -2, ('Y', 'I'): -1, ('Y', 'E'): -2, ('B', 'Y'): -3,
             ('Y', 'A'): -2,
             ('V', 'D'): -3, ('B', 'S'): 0, ('Y', 'Y'): 7, ('G', 'N'): 0, ('E', 'C'): -4, ('Y', 'Q'): -1, ('Z', 'Z'): 4,
             ('V', 'A'): 0, ('C', 'C'): 9, ('M', 'R'): -1, ('V', 'E'): -2, ('T', 'N'): 0, ('P', 'P'): 7, ('V', 'I'): 3,
             ('V', 'S'): -2, ('Z', 'P'): -1, ('V', 'M'): 1, ('T', 'F'): -2, ('V', 'Q'): -2, ('K', 'K'): 5,
             ('P', 'D'): -1,
             ('I', 'H'): -3, ('I', 'D'): -3, ('T', 'R'): -1, ('P', 'L'): -3, ('K', 'G'): -2, ('M', 'N'): -2,
             ('P', 'H'): -2,
             ('F', 'Q'): -3, ('Z', 'G'): -2, ('X', 'L'): -1, ('T', 'M'): -1, ('Z', 'C'): -3, ('X', 'H'): -1,
             ('D', 'R'): -2,
             ('B', 'W'): -4, ('X', 'D'): -1, ('Z', 'K'): 1, ('F', 'A'): -2, ('Z', 'W'): -3, ('F', 'E'): -3,
             ('D', 'N'): 1,
             ('B', 'K'): 0, ('X', 'X'): -1, ('F', 'I'): 0, ('B', 'G'): -1, ('X', 'T'): 0, ('F', 'M'): 0, ('B', 'C'): -3,
             ('Z', 'I'): -3, ('Z', 'V'): -2, ('S', 'S'): 4, ('L', 'Q'): -2, ('W', 'E'): -3, ('Q', 'R'): 1,
             ('N', 'N'): 6,
             ('W', 'M'): -1, ('Q', 'C'): -3, ('W', 'I'): -3, ('S', 'C'): -1, ('L', 'A'): -1, ('S', 'G'): 0,
             ('L', 'E'): -3,
             ('W', 'Q'): -2, ('H', 'G'): -2, ('S', 'K'): 0, ('Q', 'N'): 0, ('N', 'R'): 0, ('H', 'C'): -3,
             ('Y', 'N'): -2,
             ('G', 'Q'): -2, ('Y', 'F'): 3, ('C', 'A'): 0, ('V', 'L'): 1, ('G', 'E'): -2, ('G', 'A'): 0, ('K', 'R'): 2,
             ('E', 'D'): 2, ('Y', 'R'): -2, ('M', 'Q'): 0, ('T', 'I'): -1, ('C', 'D'): -3, ('V', 'F'): -1,
             ('T', 'A'): 0,
             ('T', 'P'): -1, ('B', 'P'): -2, ('T', 'E'): -1, ('V', 'N'): -3, ('P', 'G'): -2, ('M', 'A'): -1,
             ('K', 'H'): -1,
             ('V', 'R'): -3, ('P', 'C'): -3, ('M', 'E'): -2, ('K', 'L'): -2, ('V', 'V'): 4, ('M', 'I'): 1,
             ('T', 'Q'): -1,
             ('I', 'G'): -4, ('P', 'K'): -1, ('M', 'M'): 5, ('K', 'D'): -1, ('I', 'C'): -1, ('Z', 'D'): 1,
             ('F', 'R'): -3,
             ('X', 'K'): -1, ('Q', 'D'): 0, ('X', 'G'): -1, ('Z', 'L'): -3, ('X', 'C'): -2, ('Z', 'H'): 0,
             ('B', 'L'): -4,
             ('B', 'H'): 0, ('F', 'F'): 6, ('X', 'W'): -2, ('B', 'D'): 4, ('D', 'A'): -2, ('S', 'L'): -2, ('X', 'S'): 0,
             ('F', 'N'): -3, ('S', 'R'): -1, ('W', 'D'): -4, ('V', 'Y'): -1, ('W', 'L'): -2, ('H', 'R'): 0,
             ('W', 'H'): -2,
             ('H', 'N'): 1, ('W', 'T'): -2, ('T', 'T'): 5, ('S', 'F'): -2, ('W', 'P'): -4, ('L', 'D'): -4,
             ('B', 'I'): -3,
             ('L', 'H'): -3, ('S', 'N'): 1, ('B', 'T'): -1, ('L', 'L'): 4, ('Y', 'K'): -2, ('E', 'Q'): 2,
             ('Y', 'G'): -3,
             ('Z', 'S'): 0, ('Y', 'C'): -2, ('G', 'D'): -1, ('B', 'V'): -3, ('E', 'A'): -1, ('Y', 'W'): 2,
             ('E', 'E'): 5,
             ('Y', 'S'): -2, ('C', 'N'): -3, ('V', 'C'): -1, ('T', 'H'): -2, ('P', 'R'): -2, ('V', 'G'): -3,
             ('T', 'L'): -1,
             ('V', 'K'): -2, ('K', 'Q'): 1, ('R', 'A'): -1, ('I', 'R'): -3, ('T', 'D'): -1, ('P', 'F'): -4,
             ('I', 'N'): -3,
             ('K', 'I'): -3, ('M', 'D'): -3, ('V', 'W'): -3, ('W', 'W'): 11, ('M', 'H'): -2, ('P', 'N'): -2,
             ('K', 'A'): -1,
             ('M', 'L'): 2, ('K', 'E'): 1, ('Z', 'E'): 4, ('X', 'N'): -1, ('Z', 'A'): -1, ('Z', 'M'): -1,
             ('X', 'F'): -1,
             ('K', 'C'): -3, ('B', 'Q'): 0, ('X', 'B'): -1, ('B', 'M'): -3, ('F', 'C'): -2, ('Z', 'Q'): 3,
             ('X', 'Z'): -1,
             ('F', 'G'): -3, ('B', 'E'): 1, ('X', 'V'): -1, ('F', 'K'): -3, ('B', 'A'): -2, ('X', 'R'): -1,
             ('D', 'D'): 6,
             ('W', 'G'): -2, ('Z', 'F'): -3, ('S', 'Q'): 0, ('W', 'C'): -2, ('W', 'K'): -3, ('H', 'Q'): 0,
             ('L', 'C'): -1,
             ('W', 'N'): -4, ('S', 'A'): 1, ('L', 'G'): -4, ('W', 'S'): -3, ('S', 'E'): 0, ('H', 'E'): 0,
             ('S', 'I'): -2,
             ('H', 'A'): -2, ('S', 'M'): -1, ('Y', 'L'): -1, ('Y', 'H'): 2, ('Y', 'D'): -3, ('E', 'R'): 0,
             ('X', 'P'): -2,
             ('G', 'G'): 6, ('G', 'C'): -3, ('E', 'N'): 0, ('Y', 'T'): -2, ('Y', 'P'): -3, ('T', 'K'): -1,
             ('A', 'A'): 4,
             ('P', 'Q'): -1, ('T', 'C'): -1, ('V', 'H'): -3, ('T', 'G'): -2, ('I', 'Q'): -3, ('Z', 'T'): -1,
             ('C', 'R'): -3,
             ('V', 'P'): -2, ('P', 'E'): -1, ('M', 'C'): -1, ('K', 'N'): 0, ('I', 'I'): 4, ('P', 'A'): -1,
             ('M', 'G'): -3,
             ('T', 'S'): 1, ('I', 'E'): -3, ('P', 'M'): -2, ('M', 'K'): -1, ('I', 'A'): -1, ('P', 'I'): -3,
             ('R', 'R'): 5,
             ('X', 'M'): -1, ('L', 'I'): 2, ('X', 'I'): -1, ('Z', 'B'): 1, ('X', 'E'): -1, ('Z', 'N'): 0, ('X', 'A'): 0,
             ('B', 'R'): -1, ('B', 'N'): 3, ('F', 'D'): -3, ('X', 'Y'): -1, ('Z', 'R'): 0, ('F', 'H'): -1,
             ('B', 'F'): -3,
             ('F', 'L'): 0, ('X', 'Q'): -1, ('B', 'B'): 4}

    def get_distance_matrix(self):
        return self.distance_matrix

class Score:
    """ Class representing MSA (Multiple Sequence Alignment) scores

    A msa has to be a Python list containing pairs of (identifier, sequence), as in this example:
    ((id1, SSSBA), (id2, HHALK), (id3, -HLGS), etc))

    Requirements:
    - All the sequences in an msa must be aligned
    - The gap character is '-'

    """

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


class Entropy(Score):
    def __init__(self):
        pass

    def compute(self, msa):
        """Compute minimum entropy for a MSA

        This function redefines the inherited function from Score (Parent Class).
        From multiple alignment sequences, it calculates the score of the column similarity
        using the Minimum Entropy formula.

        :param msa: MSA list of tuples
        :return score: Total score of MSA after calculating Minimum Entropy for each column
        """

        logger.debug('Computing score...')
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
            dict[character] = column.count(character) / len(column)

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


class PercentageOfNonGaps(Score):
    def __init__(self, msa):
        self.msa = msa

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
        logger.info('Total number of non-gaps: {0}'.format(tamVal * 2 - t))
        return 100 - (t / (tamVal * len(sequences)) * 100)


class PercentageOfTotallyConservedColumns(Score):
    def __init__(self, msa):
        self.msa = msa

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
            logger.debug('[-] Score of {0} and {1}: {2}'.format(most_frequent_char, char,
                                                                self.get_score_of_two_chars(most_frequent_char, char)))

        logger.debug('[-] Score of column: {0}'.format(score_of_column))

        return score_of_column

    def get_score_of_two_chars(self, charA, charB):
        """ Return the score of two chars using the substituion matrix.

        :param charA: First char.
        :param charB: Second char.
        :return: Value of the score.
        """

        return int(self.substitution_matrix.get_distance(charA, charB))


class SumOfPairs(Score):
    """ Class for returning the alignment score of >1 sequences given the substituion matrix. """

    def __init__(self, substitution_matrix):
        self.substitution_matrix = substitution_matrix

    def compute(self, msa):
        """ Compute the score of two or more sequences using the "Sum of Pairs" method.

        :param msa: List of pairs -id and sequence- (i.e. "[('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]" ).
        :return: List of sequences.
        """

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
        """ Compare each element of the list 'column' with the others only one time.

        :param column: List of chars.
        :return: Score of two chars.
        """

        score_of_column = 0

        for charA, charB in self.possible_combinations(column):
            score_of_column += self.get_score_of_two_chars(charA, charB)
            logger.debug(
                '[-] Score of {0} and {1}: {2}'.format(charA, charB, self.get_score_of_two_chars(charA, charB)))

        logger.debug('[-] Score of column: {0}'.format(score_of_column))

        return score_of_column

    def possible_combinations(self, column):
        """ Compare each element of the list 'column' with the others only one time.

        :param column: List of chars (i.e. ['A','B','C'].
        :return: 2-length tuples with no repeated elements.
        """
        return itertools.combinations(column, 2)

    def get_score_of_two_chars(self, charA, charB):
        """ Return the score of two chars using the substituion matrix.

        :param charA: First char.
        :param charB: Second char.
        :return: Value of the score.
        """

        return int(self.substitution_matrix.get_distance(charA, charB))


class SumOfPairsTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")
        self.sumofpairs_PAM250 = SumOfPairs(PAM250())
        self.sumofpairs_Blosum62 = SumOfPairs(Blosum62())

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_basic_score_of_12_with_PAM250(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', 'AA'), ('ID2', 'AA'), ('ID3', 'AA')]

        # results
        result = self.sumofpairs_PAM250.compute(msa)
        expected = 12

        # check
        self.assertEqual(expected, result)

    def test_basic_score_of_12_with_BLOSUM62(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', 'AA'), ('ID2', 'AA'), ('ID3', 'AA')]

        # results
        result = self.sumofpairs_Blosum62.compute(msa)
        expected = 24

        # check
        self.assertEqual(expected, result)

    def test_basic_score_with_gaps_BLOSUM62(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', 'FA'), ('ID2', 'A-')]

        # results
        result = self.sumofpairs_Blosum62.compute(msa)
        expected = -10

        # check
        self.assertEqual(expected, result)

    def test_only_gaps_with_BLOSUM62(self):
        logger.info("Test for compute()...")

        # setup
        msa = [('ID1', '---'), ('ID2', '---')]

        # results
        result = self.sumofpairs_Blosum62.compute(msa)
        expected = 3

        # check
        self.assertEqual(expected, result)

    def test_get_score_of_A_and_gap(self):
        logger.info("Test for get_score_of_two_chars()...")

        # setup
        charA, charB = 'A', '-'

        # results
        result = self.sumofpairs_Blosum62.get_score_of_two_chars(charA, charB)
        expected = -8

        # check
        self.assertEqual(expected, result)

    def test_get_score_of_column_with_only_gaps(self):
        logger.info("Test for get_score_of_k_column()...")

        # setup
        column = ['-', '-', '-']

        # results
        result = self.sumofpairs_Blosum62.get_score_of_k_column(column)
        expected = 3

        # check
        self.assertEqual(expected, result)


class StarTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")
        self.star_PAM250 = Star(PAM250())
        self.star_Blosum62 = Star(Blosum62())

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_most_frequent_A_with_BLOSUM62(self):
        logger.info("Test for test_most_frequent_with_BLOSUM62()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_Blosum62.compute(msa)
        expected = 30

        # check
        self.assertEqual(expected, result)

    def test_most_frequent_error_with_BLOSUM62(self):
        logger.info("Test for test_most_frequent_error_with_BLOSUM62()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_Blosum62.compute(msa)
        expected = 22

        # check
        with self.assertRaises(Exception):
            self.assertEqual(expected, result)

    def test_most_frequent_with_PAM250(self):
        logger.info("Test for test_most_frequent_with_PAM250()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_PAM250.compute(msa)
        expected = 28

        # check
        self.assertEqual(expected, result)

    def test_most_frequent_error_with_PAM250(self):
        logger.info("Test for test_most_frequent_error_with_PAM250()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'AC'), ('sec3', 'AC')]

        # results
        result = self.star_PAM250.compute(msa)
        expected = 22

        # check
        with self.assertRaises(Exception):
            self.assertEqual(expected, result)

    def test_most_frequent_gaps_with_PAM250(self):
        logger.info("Test for test_most_frequent_gaps_with_PAM250()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'A-'), ('sec3', 'AC')]

        # results
        result = self.star_PAM250.compute(msa)
        expected = -2

        # check
        self.assertEqual(expected, result)

    def test_most_frequent_gaps_with_BLOSUM62(self):
        logger.info("Test for test_most_frequent_gaps_with_BLOSUM62()...")

        # setup
        msa = [('sec1', 'AA'), ('sec2', 'A-'), ('sec3', 'AC')]

        # results
        result = self.star_Blosum62.compute(msa)
        expected = 8

        # check
        self.assertEqual(expected, result)

class PercentageOfTotallyConservedColumnsTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_percentage_of_totally_conserved_columns_100(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_100()...")

        # setup
        msa = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfTotallyConservedColumns(msa)

        # results
        result = self.per.percentage_of_totally_conserved_columns()
        expected = 100

        # check
        self.assertEqual(result, expected)



class PercentageOfNonGapsTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_percentage_of_non_gaps_100(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_100()...")

        # setup
        msa = [["S1", "AdddAAA"], ["S2", "AdddAAA"]]
        self.per = PercentageOfNonGaps(msa)

        # results
        result = self.per.percentage_of_non_gaps()
        expected = 100

        # check
        self.assertEqual(result, expected)

    def test_percentage_of_non_gaps_50(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_50()...")

        # setup
        msa = [["S1", "---dAAA"], ["S2", "Add----"]]
        self.per = PercentageOfNonGaps(msa)

        # results
        result = self.per.percentage_of_non_gaps()
        expected = 50

        # check
        self.assertEqual(result, expected)

    def test_percentage_of_non_gaps_0(self):
        logger.info("Test for test_percentage_of_totally_conserved_columns_0()...")

        # setup
        msa = [["S1", "------"], ["S2", "------"]]
        self.per = PercentageOfNonGaps(msa)

        # results
        result = self.per.percentage_of_non_gaps()
        expected = 0

        # check
        self.assertEqual(result, expected)


class EntropyTestCases(unittest.TestCase):
    def setUp(self):
        print("setUp: RUNNING TEST")
        self.ent = Entropy()

    def tearDown(self):
        print("tearDown: TEST ENDED")

    def test_get_entropy_of_a_column_with_gaps(self):
        logger.info("Test for test_get_entropy_of_a_column_with_gaps()...")

        # setup
        d = {"-": 0.8, "A": 0.2}

        # results
        result = round(self.ent.get_column_entropy(d), 1)
        expected = -0.5

        # check
        self.assertEqual(expected, result)

    def test_get_entropy_of_a_gapped_column(self):
        logger.info("Test for test_get_entropy_of_a_gapped_column()...")

        # setup
        d = {"-": 1}

        # results
        expected = 0
        result = self.ent.get_column_entropy(d)

        # check
        self.assertEqual(expected, result)

    def test_get_dictionary_of_a_five_letter_column(self):
        logger.info("Test for test_get_dictionary_of_a_five_letter_column()...")

        # setup
        column = ("-", "A", "C", "G", "T")
        tot_seqs = len(column)

        # results
        expected = {"-": 1 / tot_seqs, "A": 1 / tot_seqs, "C": 1 / tot_seqs, "G": 1 / tot_seqs, "T": 1 / tot_seqs}
        result = self.ent.get_frecuencies(column)

        # check
        self.assertEqual(expected, result)

    def test_get_dictionary_of_a_gapped_column(self):
        logger.info("Test for test_get_dictionary_of_a_gapped_column()...")

        # setup
        column = ("-", "-", "-", "-", "-")

        # results
        expected = {"-": 1}
        result = self.ent.get_frecuencies(column)

        # check
        self.assertEqual(expected, result)

    def test_compute_of_four_seqs_with_no_gaps(self):
        logger.info("Test for test_compute_of_four_seqs_with_no_gaps()...")

        # setup
        msa = [("S1", "ACGT"), ("S2", "ACGT"), ("S3", "TGCA"), ("S4", "TGCA")]

        # results
        expected = -2.77
        result = round(self.ent.compute(msa), 2)

        # check
        self.assertEqual(expected, result)

    def test_compute_of_three_seqs_with_gaps(self):
        logger.info("Test for test_compute_of_three_seqs_with_gaps()...")

        # setup
        msa = [("S1", "A-TGCAAT-G"), ("S2", "-CT-CCAT-A"), ("S3", "-TTAT-CTG-")]

        # results
        expected = -6.94
        result = round(self.ent.compute(msa), 2)

        # check
        self.assertEqual(expected, result)

    def test_compute_of_two_gapped_seqs(self):
        logger.info("Test for test_compute_of_two_gapped_seqs()...")

        # setup
        msa = [("S1", "-----"), ("S2", "-----")]

        # results
        expected = 0
        result = self.ent.compute(msa)

        # check
        self.assertEqual(expected, result)


if __name__ == "__main__":
    unittest.main()
