from pymsascoring.score import Score
import math

__author__ = "Pablo Rodríguez"
__copyright__ = ""
__credits__ = ["Pablo Rodríguez", "Guillermo López"]
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = ["pabrod@uma.es", "guilopgar@uma.es"]

class Entropy(Score):

    def __init__(self):
        pass

    def compute(self, msa):
        """Compute minimum entropy for a MSA

        This function redefines the inherited function from Score (Parent Class).
        From multiple alignment sequences, it calculates the score of the column similarity
        using the Minimum Entropy formula.

        :param msa: - MSA list of tuples
        :return score: - Total score of MSA after calculating Minimum Entropy for each column
        """
        n_cols = len(msa[0][1])                             # NUMBER OF CHARACTERS OF EVERY SEQUENCE
        total_seqs = len(msa)                               # NUMBER OF SEQUENCES TO COMPARE
        score = 0                                             # RETURN VALUE

        for i in range(n_cols):
            char_dict = self.get_dictionary(msa, i, total_seqs)
            current_entropy = self.get_column_entropy(char_dict)
            score+=current_entropy
        
        return score


    def get_dictionary(self, list, pos, tot_seq):
        """
        Get Dictionary of characters for the MSA list at current position

        :param list: - MSA list of tuples
        :param pos: - Current column to be analyzed
        :param tot_seq: - Number of sequences in the MSA

        :return dict: - Dictionary in which the Keys are characters and the Value is the frequency that key appears on the current column
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
        """Calculates the Minimum Entropy for the current column dictionary

        :param dict: - Dictionary in which the Keys are characters and the Value is the frequency that key appears on the current column

        :return current_entropy: - Minimum Entropy score of the current column
        """
        current_entropy = 0

        for k in dict.keys():
            f = dict[k]
            current_entropy += f * math.log(f)

        return current_entropy
