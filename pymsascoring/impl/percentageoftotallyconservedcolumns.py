
#Author:Juan Ignacio Álvarez

from pymsascoring.score import Score

class PercentageOfTotallyConservedColumns(Score):
    list = []

    def __init__(self, a):
        self.list = a

    def percentage_of_totally_conserved_columns(self):
    #We assume that all sequences have the same length if not so it will be analyzed only up to the length of the first
        count = 0
        h = 0
        model=self.list[0]
    #Recorre each letter of the secuencies
        while h < len(model[1]):
            count2 = 0
        #Recorre each secuence
            for u in self.list:
                temp = model[1]
                temp2 = u[1]
                #Comparing and count
                if temp[h] == temp2[h] and temp2[h] != "-":
                    count2 += 1
                    if count2 == len(self.list):
                        count += 1
            h += 1
        return count / len(model[1]) * 100;