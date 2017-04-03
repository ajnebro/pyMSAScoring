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
"""
    ----------------------------
    Author: Pablo Rodríguez
    ----------------------------
"""

from pymsascoring.score import Score
import math

class Entropy(Score):

    def __init__(self):
        pass

    def compute(self, msa):
        """
        This function redefines the inherited function from Score (Parent Class).
        From multiple alignment sequences, it calculates the score of the column similarity
            using the Minimum Entropy formula.
        """
        n_cols = len(msa[0][1])                             # NUMBER OF CHARACTERS OF EVERY SEQUENCE
        total_seqs = len(msa)                               # NUMBER OF SEQUENCES TO COMPARE
        sum = 0                                             # RETURN VALUE

        for i in range(n_cols):
            char_dict = self.get_dictionary(msa, i, total_seqs)
            current_entropy = self.get_column_entropy(char_dict)
            sum+=current_entropy
        
        return sum


    def get_dictionary(self, list, pos, tot_seq):
        """
        Get Dictionary of characters for the MSA list at current position
        """
        dict = {}
        curr_chars = [0] * tot_seq
        j=0
        for item in list:
            curr_chars[j] = item[1][pos]
            if curr_chars[j] not in dict:
                dict[curr_chars[j]] = 1/tot_seq
            else:
                dict[curr_chars[j]] += 1 / tot_seq
            j+=1

        return dict

    def get_column_entropy(self, dict):
        """
        Calculates the Minimum Entropy for the current column dictionary
        """
        current_entropy = 0

        for k in dict.keys():
            f = dict[k]
            current_entropy += f * math.log(f)

        return current_entropy
