"""

"""

from pymsascoring.score import Score
import math

class Entropy (Score):
    list=[]
    
    def __init__(self, l):
        self.list=l
    
    def calculate_minimum_entropy(self):
        sum = 0                     #RETURN VALUE
        maxCol = 0                  #MAXIMUM COLUMNS FOR SEQUENCE
        total_seqs = len(list)      #NUMBER OF SEQUENCES TO COMPARE
        
        
        
        #SET MAX COLUMN LENGTH
        for item in list:
            currLen = len(item[1])
            if currLen > maxCol:
                maxCol= currLen
                
        #CALCULATE ENTROPY FOR ALL CHARS IN SEQUENCE AND SUM TOTAL
        for i in range(maxCol):
            curr_chars = []                                 #INIT CURRENT CHARACTER ARRAY
            curr_chars[total_seqs] = [0]*len(total_seqs)    #SET CURRENT CHAR ARRAY TO ZERO
            
            #GET ALL CHARS FOR CURRENT POSITION
            j=0
            for item in list:
                curr_chars[j]=item[1][i]
                j+=1
                
            #CREATE DICTIONARY FOR CURRENT POSITION (KEY=CHAR, VALUE=TIMES)
            diff_chars = {}
            for j in range(total_seqs):
                if curr_chars[j] not in diff_chars:
                    diff_chars[curr_chars[j]] = 1
                else:
                    diff_chars[curr_chars[j]] += 1
            
            #CREATE FREQUENCIES FOR EACH KEY IN DICTIONARY
            k=0
            frequencies = []
            for kv in diff_chars.items():
                frequencies[k] = kv[1]/total_seqs
                k += 1
            
            #CALCULATE CURRENT ENTROPY
            current_entropy = 0
            for char in len(frequencies):
                current_entropy += frequencies[char]*math.log(frequencies[char])
            
            #ADD CURRENT ENTROPY TO SUM
            sum+=current_entropy
        
        return sum