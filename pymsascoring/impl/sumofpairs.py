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


__author__ = 'Antonio Benítez, René Betancor'


class SumOfPairs(Score):
    """
    Class for returning the alignment score of >1 sequences given the substituion matrix..

    get_seq_only        Get the second value of a list with multiple elements.
    calc_score          Given two char, return the partial score.
    calc_final_socre    Get the final score of the alignment.
    """

    def __init__(self, list_of_pairs, substitution_matrix):
        self.list_of_pairs = list_of_pairs
        self.sequences = [] # list of sequences
        self.sub_matrix = substitution_matrix

    def get_seqs_only(self):
        for i in range(len(self.list_of_pairs)):  # list_of_pairs = [('ID1', 'AB'), ('ID2', 'CD'), ('ID3', 'EF')]
            self.sequences.append(self.list_of_pairs[i][1])  # values = ('AB', 'CD', 'EF' )
        return self.sequences

    def calc_final_score(self):
        sequences = self.get_seqs_only()
        tamSeq = len(sequences[0])  # length of the first sequence (= length to the second one, third one...)
        column = []
        final_score = 0

        for k in range(tamSeq):
            for sequence in sequences:
                column.append(sequence[k])  # add to 'column' the k-char of each sequence
            #print(column)  # column = ['A', 'C', 'E'] (the first time), ['-', 'D', '-'] (the second)
            for charA, charB in itertools.combinations(column, 2):  # compare each element of the list 'column' with the others only one time
                partial_score = self.get_score(charA, charB)
                final_score += + partial_score
                #print('Score of {0} and {1}: {2}'.format(charA, charB, partial_score, final_score))
            column.clear()  # clear the list for the next column

        #print('Final score: {0}'.format(final_score))
        return final_score

    def get_score(self, charA, charB):
        return int(self.sub_matrix.get_distance(charA, charB))