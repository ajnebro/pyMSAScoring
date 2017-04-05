
from pymsascoring.score import Score

__author__ = "Juan ignacio Álvarez"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "juaalvare@uma.es"

class PercentageOfNonGaps(Score):
    list = []

    def __init__(self, a):
        self.list = a

    def  percentage_of_non_gaps(self):
        """
                This function redefines count the number of non gaps of a list of MSA

                Args:
                    count - the number of totals non gaps
                    count2 - number of gaps per column
                    curr_char - colum of eash MSA
                    model - First sequence used as reference to starting the comparation
                    temp - temporal variable that contains the current sequence of the list 
                Returns:
                    score - Total score of MSA after calculating percentage of non gaps

                """
        count=0
        curr_char=0
        model=self.list[0]

        while curr_char<len(model[1]):
            count2=0

            for current_sequence in self.list:
                temp=current_sequence[1]
            # Comparing and count
                if temp[curr_char]=="-":
                    count2 +=1
            if count2==0:
                count+=1
            curr_char+=1
        return count/len(model[1])*100;