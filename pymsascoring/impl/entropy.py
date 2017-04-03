"""
This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

from pymsascoring.score import Score

"""

Author: Pablo Rodríguez

"""

import sys
sys.path.append("../")
from score import Score
import math

class Entropy (Score):
    list=[]
    
    def __init__(self, l):
        self.list=l
    
    def compute(self):
        sum = 0                                                 #RETURN VALUE
        n_cols = len(self.list[0][1])                           #NUMBER OF CHARACTERS OF EVERY SEQUENCE
        total_seqs = len(self.list)                             #NUMBER OF SEQUENCES TO COMPARE
        
        # CALCULATE ENTROPY FOR ALL CHARS IN SEQUENCE AND SUM TOTAL
        for i in range(n_cols):
            curr_chars = [0] * total_seqs                       #SET CURRENT CHAR LIST TO ZERO
            
            ### GET ALL CHARS FOR CURRENT POSITION
            j=0                                                 #SEQUENCE COUNTER FOR CURRENT CHAR ARRAY
            ### CREATE DICTIONARY FOR CURRENT POSITION (KEY=CHAR, VALUE=RELATIVE FREQUENCY)
            diff_chars = {}                                     # INIT DICTIONARY
            for item in self.list:
                curr_chars[j]=item[1][i]                        #SET CURRENT CHAR FOR SEQUENCE
                if curr_chars[j] not in diff_chars:             #IF CHAR IS NOT IN DICT, CREATE KEY
                    diff_chars[curr_chars[j]] = 1/total_seqs
                else:
                    diff_chars[curr_chars[j]] += 1/total_seqs   #ELSE ADD 1/TOTAL_SEQS TO VALUE FOR KEY
                j+=1
            
            ### CALCULATE CURRENT COLUMN ENTROPY
            current_entropy = 0
            for k in diff_chars.keys():
                #CALCULATE ENTROPY FOR CURRENT CHARACTER
                f = diff_chars[k]
                current_entropy += f*math.log(f)
            
            #ADD CURRENT COLUMN ENTROPY TO SUM
            sum+=current_entropy
        
        return sum
