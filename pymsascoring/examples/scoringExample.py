from pymsascoring.distancematrix.impl.blosum62 import Blosum62
from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.score.impl.entropy import Entropy
from pymsascoring.score.impl.sumofpairs import SumOfPairs
from pymsascoring.score.score import Score

__author__ = "Antonio J. Nebro"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "antonio@lcc.uma.es"

"""
This program is intended to show some examples of using the scores in pyMSA.
"""

def compute_score(score : Score, msa) -> float:
    return score.compute(msa)

if __name__ == '__main__':

    msa = (("s1", "ACTG"), ("S2", "A-T-"))

    score_method = Entropy()
    value = compute_score(score_method, msa)
    print(value)

    score_method = SumOfPairs(Blosum62())
    value = compute_score(score_method, msa)
    print(value)

    score_method = SumOfPairs(PAM250())
    value = compute_score(score_method, msa)
    print(value)