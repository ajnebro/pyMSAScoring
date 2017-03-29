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