

from pymsascoring.score.score import Score

__author__ = "Juan ignacio Álvarez"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "juaalvare@uma.es"

class PercentageOfTotallyConservedColumns(Score):
    list = []

    def __init__(self, a):
        self.list = a

    def percentage_of_totally_conserved_columns(self):
        """
                        This function redefines count the number of conserved columns of a list of MSA

                        Args:
                            count - the number of totals conserved columns
                            count2 - number of equals letters  per column
                            curr_char - colum of each MSA
                            model - First sequence used as reference to starting the comparation
                        Returns:
                            score - Total score of MSA after calculating percentage of non gaps

                        """
        count = 0
        curr_char = 0
        model=self.list[0]
    #Iterate each letter of the secuencies
        while curr_char < len(model[1]):
            count2 = 0
        #Iterate each secuence
            for current_sequence in self.list:
                temp = model[1]
                temp2 = current_sequence[1]
                #Comparing and count
                if temp[curr_char] == temp2[curr_char] and temp2[curr_char] != "-":
                    count2 += 1
                    if count2 == len(self.list):
                        count += 1
            curr_char += 1
        return count / len(model[1]) * 100;