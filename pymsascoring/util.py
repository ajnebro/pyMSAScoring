from itertools import islice


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

    def save_fasta_serialized(fileName):
        with open("serialized.txt", 'w') as output:
            list = ReadFastaFile.read_fasta_file_as_list_of_pairs(fileName)

            for (pair1, pair2) in list:
                output.write(pair1 + ',' + pair2 + '\n')


class ReadFastqFile():
    """
    Read a FASTQ file and return a list of pairs -->  [(key, value), (key, value)]
    """
    def read_fastq_file_as_list_of_pairs(filename):
        vector = []
        key = ''
        value = ''
        groups = []
        with open(filename, 'r') as file:
            for line in file:
                if len(groups) == 4:
                    key = groups[0][1:].rstrip()
                    value = groups[1].rstrip()
                    groups = []
                    vector.append((key, value))
                groups.append(line)
        key = groups[0][1:].rstrip()
        value = groups[1].rstrip()
        vector.append((key, value))
        file.close()
        return vector
