from pymsascoring.score import Score
import operator
from collections import Counter
__author__ = "Daniel Torres Ramírez"
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

        secuencias = self.get_seqs_only()

        posiciones = []
        elementosMasFrecuentesyNumeroRepeticones = []
        elementosMasFrecuentesyNumeroRepeticonesArreglada = []
        SoloElementos = []
        final = []
        result = 0
        for secuencia in secuencias:  # we select each list from our list of list
            for i, c1 in enumerate(secuencia):
                posiciones.append((i, c1))  # we obtain for each element one position

        posicionSort = sorted(posiciones, key=operator.itemgetter(0))  # sort our list depending of the position
        list2 = [item[1] for item in posicionSort]  # we build a new list using just the characters
        listaDeCaracteres = [list2[i:i + len(secuencias)] for i in
                             range(0, len(list2), len(secuencias))]  # For each position we will group the elements.

        # this select the most frecuence element for each position
        for x in listaDeCaracteres:
            a = Counter(x).most_common(1)
            elementosMasFrecuentesyNumeroRepeticones.append(a)
        for secuencia in elementosMasFrecuentesyNumeroRepeticones:
            for secuencia1 in secuencia:
                elementosMasFrecuentesyNumeroRepeticonesArreglada.append((secuencia1))
        SoloElementos = [item[0] for item in elementosMasFrecuentesyNumeroRepeticonesArreglada]

        # this will associate the most frecuence element with all the elements of the same position

        for i, secuencias in enumerate(listaDeCaracteres):
            for caracteres in secuencias:
                for j, masFrecuente in enumerate(SoloElementos):
                    if i == j:
                        final.append((masFrecuente, caracteres))
        # We will obtain the score for each tuple
        for tupla in final:
            charA = tupla[0]
            charB = tupla[1]
            partial_score = self.calc_score(charA, charB)
            result += + partial_score
        return result

    def calc_score(self, charA, charB):
        return int(self.distancematrix.get_distance(charA, charB))

