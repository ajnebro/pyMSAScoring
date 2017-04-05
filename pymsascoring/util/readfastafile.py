__author__ = "Maria Jose Muñoz"
__copyright__ = ""
__credits__ = ["Maria Jose Muñoz"]
__license__ = "GPL"
__version__ = "1.0"
__status__ = "Development"
__email__ = ["marmungon@uma.es"]

class ReadFastaFile():
    """
    Read a Fasta file and return a list of pairs --> [(key, value), (key, value)]
    """
    def read_fasta_file_as_list_of_pairs(fileName):
        vector = []
        key = ''
        value = ''
        with open(fileName, 'r') as file:
            for line in file:
                if line[0] == '>':
                    if key != '':
                        vector.append((key, value))
                    key = line[1:].rstrip()
                    value = ''  # aun no hemos leido ninguna secuencia
                else:
                    value += line.rstrip()
        vector.append((key, value))
        file.close()
        return vector