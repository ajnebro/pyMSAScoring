import operator
from collections import Counter
from Bio.SubsMat import MatrixInfo
from pymsascoring.score import Score

class Star(Score):
 SecuenciaEIdentificador = []

 def __init__(self,l):
       self.SecuenciaEIdentificador = l

 def sumStar(self):

        secuencias=[item[1] for item in self.SecuenciaEIdentificador]
        posiciones=[]
        elementosMasFrecuentesyNumeroRepeticones=[]
        elementosMasFrecuentesyNumeroRepeticonesArreglada=[]
        SoloElementos=[]
        final=[]
        resultado=0
        matriz=MatrixInfo.blosum65



        for secuencia in secuencias:
            for i,c1 in enumerate(secuencia):
                posiciones.append((i,c1))

        posicionSort=sorted(posiciones, key=operator.itemgetter(0))  #nos ordena la lista
        list2=[item[1] for item in posicionSort] #creamos una lista de caracteres con la lista ordenada anteriormente
        listaDeCaracteres=[list2[i:i+len(secuencias)] for i  in range(0, len(list2), len(secuencias))]#con esto creamos una lista por cada posicion para i=0 tendra 4 elementos J,A,G,T


        for x in listaDeCaracteres:
           a=Counter(x).most_common(1)
           elementosMasFrecuentesyNumeroRepeticones.append(a)
        for secuencia in elementosMasFrecuentesyNumeroRepeticones:
            for secuencia1 in secuencia:
                elementosMasFrecuentesyNumeroRepeticonesArreglada.append((secuencia1))
        SoloElementos=[item[0] for item in elementosMasFrecuentesyNumeroRepeticonesArreglada]

         #lista de los elementos mas frecuentes con el numero de veces que se repiten para i=0 el elementos que mas se repite es A y se repite dos veces y asi con todos

        for i,secuencias in enumerate(listaDeCaracteres):
            for caracteres in secuencias:
                for j,masFrecuente in enumerate(SoloElementos):
                    if i==j:
                        final.append((masFrecuente,caracteres))

        for i,j in final:
             if i is '-' and j==i:
                 resultado=resultado+1
             if i  is '-' and j!=i:
                 resultado=resultado-8
             if j is '-' and i!=j:
                 resultado=resultado-8


        for i in final:
            for key in matriz:

                if i==key:
                    resultado=resultado+ matriz[key]
        return resultado


