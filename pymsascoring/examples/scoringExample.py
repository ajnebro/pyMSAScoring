from pymsascoring.score import Score
from pymsascoring.impl.entropy import Entropy
from pymsascoring.impl.sumofpairs import SumOfPairs


def compute_score(score : Score, msa) -> float:
    return score.compute(msa)


if __name__ == '__main__':
    msa = (("s1", "ACTG"), ("S2", "A-T-"))

    score_method = Entropy()
    value = compute_score(score_method, msa)

    score_method = SumOfPairs()
    value = compute_score(score_method, msa)
