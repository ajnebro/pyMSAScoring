from pymsascoring.substitutionmatrix.impl.blosum62 import Blosum62
from pymsascoring.substitutionmatrix.impl.pam250 import PAM250
from pymsascoring.score.impl.entropy import Entropy
from pymsascoring.score.impl.sumofpairs import SumOfPairs
from pymsascoring.score.score import Score
from pymsascoring.score.impl.percentageofnongaps import PercentageOfNonGaps
from pymsascoring.score.impl.percentageoftotallyconservedcolumns import PercentageOfTotallyConservedColumns

__author__ = "Antonio J. Nebro"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "antonio@lcc.uma.es"

"""
This program is intended to show some examples of using the scores in pyMSA.
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
    #msa = (("a", "A"), ("b", "A"), ("c", "G"), ("d", "A"), ("e", "T"))

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