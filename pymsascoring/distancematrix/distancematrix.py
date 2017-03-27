class DistanceMatrix:

    def __init__(self, gap_penalty=-8):
        self.gap_penalty = gap_penalty

    def get_distance_matrix(self):
        pass

    def get_distance(self, char1, char2):
        if char1 is '-' and char2 is '-':
            result = 1
        elif char1 is '-' or char2 is '-':
            result = self.gap_penalty
        else:
            result = self.distance_matrix((char1, char2))


        return result

    def get_gap_penalty(self) -> float:
        return self.gap_penalty