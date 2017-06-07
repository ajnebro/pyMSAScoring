from pymsascoring.score import Score, Entropy, PercentageOfNonGaps, PercentageOfTotallyConservedColumns, Star, \
    SumOfPairs
from pymsascoring.substitutionmatrix import PAM250, Blosum62

"""
This program is intended to show some examples of using the scores in pyMSAScoring.
"""


def compute_score(score : Score, msa) -> float:
    """
    This function applies an score to a multiple sequence alignment
    :param score: 
    :param msa: 
    :return: the score value
    """
    return score.compute(msa)

if __name__ == '__main__':
    msa = (("s1", "ACTG"), ("S2", "A-T-"))

    pong = PercentageOfNonGaps(msa)
    ping = PercentageOfTotallyConservedColumns(msa)
    percentage = pong.percentage_of_non_gaps()
    conserved = ping.percentage_of_totally_conserved_columns()
    print("Percentage of non-gaps: {0} %".format(percentage))
    print("Percentage of totally conserved columns: {0}".format(conserved))

    score_method = Entropy()
    value = compute_score(score_method, msa)
    print("Entropy score: {0}".format(value))

    score_method = SumOfPairs(Blosum62())
    value = compute_score(score_method, msa)
    print("SumOfPairs score (Blosum62): {0}".format(value))

    score_method = SumOfPairs(PAM250())
    value = compute_score(score_method, msa)
    print("SumOfPairs score (PAM250): {0}".format(value))

    score_method = Star(Blosum62())
    value = compute_score(score_method, msa)
    print("Star score (Blosum62): {0}".format(value))

    score_method = Star(PAM250())
    value = compute_score(score_method, msa)
    print("Star score (PAM250): {0}".format(value))