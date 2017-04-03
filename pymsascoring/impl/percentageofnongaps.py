
#Author: Juan Ignacio Álvarez

from pymsascoring.score import Score

class PercentageOfNonGaps(Score):
    list = []

    def __init__(self, a):
        self.list = a

    def  percentage_of_non_gaps(self):
    # We assume that all sequences have the same length if not so it will be analyzed only up to the length of the first
        count=0
        h=0                 #Char position
    # Recorre each letter of the secuencies
        while h<len(self.list[1]):
            count2=0
        # Recorre each secuence
            for u in self.list:
                temp=u[1]
            # Comparing and count
                if temp[h]=="-":
                    count2 +=1
            if count2==0:
                count+=1
            h+=1
        return count/len(self.list[1])*100;