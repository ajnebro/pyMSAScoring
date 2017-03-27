"""

"""

from pymsascoring.score import Score
import math

class Entropy (Score):
    list=[]
    
    def __init__(self, l):
        self.list=l
    
    def calculate_minimum_entropy(self):
        sum = 0
        maxCol = 0
        total_seqs = len(list)
        curr_chars = []
        frequencies = []
        
        #SET MAX COLUMN LENGTH
        for item in list:
            currLen = len(item[1])
            if currLen > maxCol:
                maxCol= currLen
                
        for i in range(maxCol):
            curr_chars[total_seqs] = [0]*len(total_seqs)
            j=0
            
            for item in list:
                curr_chars[j]=item[1][i]
                j+=1
                
            diff_chars = {}
            for j in range(total_seqs):
                if curr_chars[j] not in diff_chars:
                    diff_chars[curr_chars[j]] = 1
                else:
                    diff_chars[curr_chars[j]] += 1
            
            k=0
            for kv in diff_chars.items():
                frequencies[k] = kv[1]/total_seqs
                k += 1
            
            current_entropy = 0
            for char in len(frequencies):
                current_entropy += frequencies[char]*math.log(frequencies[char])
            
            sum+=current_entropy
        
        """
        def percentage_of_totally_conserved_columns(self):
        list = self.reader.read_fasta_file_as_list_of_pairs(self.fName)
        maxCol = 0
        conserved_columns = 0
        
        for item in list:
            currLen = len(item[1])
            if currLen > maxCol:
                maxCol = currLen
        
        for i in range(maxCol):
            isConserved = True
            currLet = list[1][1][i]
            
            for item in list:
                if item[1][i] != currLet:
                    isConserved = False
                    
            if isConserved == True:
                conserved_columns+=1    
                
        return (conserved_columns/maxCol)*100
        
    def percentage_of_non_gaps(self):
        list = self.reader.read_fasta_file_as_list_of_pairs(self.fName)
        totChars = 0
        gapCounter = 0
        
        for item in list:
            currChars = len(item[1])
            totChars += currChars

            for i in range(currChars):
                if item[1][i] == '-':
                    gapCounter += 1
                    
        return 100 - (gapCounter/totChars)*100
        """