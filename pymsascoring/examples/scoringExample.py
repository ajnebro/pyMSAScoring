from pymsascoring.score import Score
from pymsascoring.impl.entropy import Entropy
from pymsascoring.impl.sumofpairs import SumOfPairs

from pymsascoring.distancematrix.impl.pam250 import PAM250
from pymsascoring.distancematrix.impl.blosum62 import Blosum62

def compute_score(score : Score, msa) -> float:
    return score.compute(msa)


if __name__ == '__main__':
    msa = (("s1", "ACTG"), ("S2", "A-T-"))

    score_method = Entropy()
    value = compute_score(score_method, msa)
    print(value)

    score_method = SumOfPairs(Blosum62)
    value = compute_score(score_method, msa)
    print(value)