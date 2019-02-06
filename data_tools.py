import os
import random

from utils import string_to_floatlist, floatlist_to_string


def _random_coords(coord_dims, min=-1e6, max=1e6):
    coords = []
    for coord in range(coord_dims):
        coords.append(random.uniform(min, max))
    return coords


def read_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(file_path + ' did not exist')

    data_list = []
    with open(file_path, mode='r') as file:
        for line in file.readlines():
            data_list.append(string_to_floatlist(line))

    return data_list


class DataGenerator(object):
    def __init__(self, directory_path, seed=1234):
        self.dir = directory_path
        random.seed(seed)

    def generate_dataset(self, num_samples, coord_dims):
        if not os.path.exists(self.dir):
            raise FileNotFoundError('Directory missing.')

        file_name = self.dir + 'sample_input_' + str(coord_dims) + '_' + str(num_samples) + '.tsv'
        with open(file_name, mode='w') as file:
            for sample in range(num_samples):
                coords = _random_coords(coord_dims)
                coords = floatlist_to_string(coords, round_to_int=False) + '\n'
                file.write(coords)
