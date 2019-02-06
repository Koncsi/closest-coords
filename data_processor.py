import os


def string_to_floatlist(parsable: str):
    string_list = parsable.split('\t')
    return [float(i) for i in string_list]

def floatlist_to_string(flist: list):
    string = ''
    for f in flist:
        string = string + str(int(round(f, 0))) + '\t'
    return string[0:-1]


class DataProcessor(object):
    def __init__(self, file_path):
        if not os.path.exists(file_path):
            raise FileNotFoundError(file_path + ' did not exist')

        self.file_path = file_path

    def read_data(self):
        data_list = []
        with open(self.file_path, mode='r') as file:
            for line in file.readlines():
                data_list.append(string_to_floatlist(line))

        return data_list


