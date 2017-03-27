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
        
        
        # SET MAX COLUMN LENGTH
        for item in list:
            currLen = len(item[1])
            if currLen > maxCol:
                maxCol= currLen
                
        # CALCULATE ENTROPY FOR ALL CHARS IN SEQUENCE AND SUM TOTAL
        for i in range(maxCol):
            curr_chars = []                                 #INIT CURRENT CHARACTER ARRAY
            curr_chars[total_seqs] = [0]*len(total_seqs)    #SET CURRENT CHAR ARRAY TO ZERO
            
            ### GET ALL CHARS FOR CURRENT POSITION
            j=0                                             #SEQUENCE COUNTER FOR CURRENT CHAR ARRAY
            for item in list:
                curr_chars[j]=item[1][i]                    #SET CURRENT CHAR FOR SEQUENCE
                j+=1
                
            ### CREATE DICTIONARY FOR CURRENT POSITION (KEY=CHAR, VALUE=TIMES)
            diff_chars = {}                                 #INIT DICTIONARY
            for j in range(total_seqs):
                if curr_chars[j] not in diff_chars:         #IF CHAR IS NOT IN DICT, CREATE KEY
                    diff_chars[curr_chars[j]] = 1
                else:
                    diff_chars[curr_chars[j]] += 1          #ELSE ADD 1 TO VALUE FOR KEY
            
            ### CREATE FREQUENCIES FOR EACH KEY IN DICTIONARY
            k=0                                             #KEY COUNTER
            frequencies = []                                #INIT FREQUENCY LIST
            for kv in diff_chars.items():
                frequencies[k] = kv[1]/total_seqs           #GET FREQUENCY FOR KEY
                k += 1
            
            ### CALCULATE CURRENT COLUMN ENTROPY
            current_entropy = 0
            for char in len(frequencies):
                #CALCULATE ENTROPY FOR CURRENT CHARACTER
                current_entropy += frequencies[char]*math.log(frequencies[char])
            
            #ADD CURRENT COLUMN ENTROPY TO SUM
            sum+=current_entropy
        
        return sum