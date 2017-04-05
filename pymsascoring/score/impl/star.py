from pymsascoring.score.score import Score
import operator

from collections import Counter
__author__ = "Daniel Torres Ramírez,Miguel Angel"
__license__ = "GNU"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "dantorram@uma.es"


class Star(Score):
    def __init__(self, list_of_pairs, DM):
        self.list_of_pairs = list_of_pairs
        self.values = []  # List for sequences
        self.distancematrix = DM

    def get_seqs_only(self):
        for i in range(len(self.list_of_pairs)):
            self.values.append(self.list_of_pairs[i][1])
        return self.values

    def sumStar(self):

        sequences = self.get_seqs_only()

        position = []
        elementMoreFrecuentAndNumberOfRepetions=[]
         
        elementMoreFrecuentAndNumberOfRepetionsFixed = []
        JustElement = []
        final = []
        result = 0
        for sequence in sequences:  # we select each list from our list of list
            for i, c1 in enumerate(sequence):
                position.append((i, c1))  # we obtain for each element one position

        posicionSort = sorted(position, key=operator.itemgetter(0))  # sort our list depending of the position
        list2 = [item[1] for item in posicionSort]  # we build a new list using just the characters
        listOfCharacters = [list2[i:i + len(sequences)] for i in
                             range(0, len(list2), len(sequences))]  # For each position we will group the elements.

        # this select the most frecuence element for each position
        for x in listOfCharacters:
            a = Counter(x).most_common(1)
            elementMoreFrecuentAndNumberOfRepetions.append(a)
        for sequence in elementMoreFrecuentAndNumberOfRepetions:
            for sequence1 in sequence:
                elementMoreFrecuentAndNumberOfRepetionsFixed.append((sequence1))
        JustElement = [item[0] for item in elementMoreFrecuentAndNumberOfRepetionsFixed]

        # this will associate the most frecuence element with all the elements of the same position

        for i, sequences in enumerate(listOfCharacters):
            for characters in sequences:
                for j, moreFrecuent in enumerate(JustElement):
                    if i == j:
                        final.append((moreFrecuent, characters))
        # We will obtain the score for each tuple
        for tuple in final:
            charA = tuple[0]
            charB = tuple[1]
            partial_score = self.calc_score(charA, charB)
            result += + partial_score
        return result

    def calc_score(self, charA, charB):
        return int(self.distancematrix.get_distance(charA, charB))

