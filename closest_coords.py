import argparse
import math

from data_tools import read_data, floatlist_to_string


def euclidean_dist(coord1: list, coord2: list):
    summ = 0
    for c1, c2 in zip(coord1, coord2):
        summ += (c1 - c2) ** 2

    return math.sqrt(summ)


def closest_coords(target_file):
    data = read_data(target_file)

    closest = (0, 0, float('inf'))

    for idx1, coord1 in enumerate(data):
        for idx2, coord2 in enumerate(data):
            distance = euclidean_dist(coord1, coord2)
            if 0 < distance < closest[2]:
                closest = (idx1, idx2, distance)

    print(f'{closest[0] + 1}:' + floatlist_to_string(data[closest[0]]))
    print(f'{closest[1] + 1}:' + floatlist_to_string(data[closest[1]]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target_file')
    args = parser.parse_args()
    closest_coords(args.target_file)
