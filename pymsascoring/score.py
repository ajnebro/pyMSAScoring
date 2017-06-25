import itertools
import logging
import math
from collections import Counter

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


class SumOfPairs(Score):
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

    def possible_combinations(self, column):
        """ Compare each element of the list 'column' with the others only one time.

        :param column: List of chars (i.e. ['A','B','C'].
        :return: 2-length tuples with no repeated elements.
        """
        return itertools.combinations(column, 2)

    def get_score_of_k_column(self, column):
        """ Compare each element of the list 'column' with the others only one time.

        :param column: List of chars.
        :return: Score of two chars.
        """

        score_of_column = 0

        for charA, charB in self.possible_combinations(column):
            score_of_column += self.get_score_of_two_chars(charA, charB)
            logger.debug('[-] Score of {0} and {1}: {2}'.format(charA, charB, self.get_score_of_two_chars(charA, charB)))

        logger.debug('[-] Score of column: {0}'.format(score_of_column))

        return score_of_column

    def get_score_of_two_chars(self, charA, charB):
        """ Return the score of two chars using the substituion matrix.

        :param charA: First char.
        :param charB: Second char.
        :return: Value of the score.
        """

        return int(self.substitution_matrix.get_distance(charA, charB))


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
        logger.info('Total number of non-gaps: {0}'.format(tamVal*2 - t))
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
