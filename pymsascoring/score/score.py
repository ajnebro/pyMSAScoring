__author__ = "Antonio J. Nebro"
__license__ = "GPL"
__version__ = "1.0-SNAPSHOT"
__status__ = "Development"
__email__ = "antonio@lcc.uma.es"

class Score:
    """ Class representing MSA (Multiple Sequence Alignment) scores
    
    A msa has to be a Python list containing pairs of (identifier, sequence), as in this example:
    ((id1, SSSBA), (id2, HHALK), (id3, -HLGS), etc)
    
    Requirements:
    - All the sequences in an msa must be aligned
    - The gap character is '-'
    
    """
    def compute(self, msa) -> float:
        """ Compute the score 
        
        :param msa
        :return: the value of the score
        """
        pass
