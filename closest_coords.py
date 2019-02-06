import argparse

from data_processor import DataProcessor, floatlist_to_string
from operations import euclidean_dist



def closest_coords(target_file):
    dp = DataProcessor(target_file)
    data = dp.read_data()

    closest_coords = (0, 0, float('inf'))
    for idx1, coord1 in enumerate(data):
        for idx2, coord2 in enumerate(data):
            distance = euclidean_dist(coord1, coord2)
            if distance > 0 and distance < closest_coords[2]:
                closest_coords = (idx1, idx2, distance)

    print(f'{closest_coords[0] + 1}:' + floatlist_to_string(data[closest_coords[0]]))
    print(f'{closest_coords[1] + 1}:' + floatlist_to_string(data[closest_coords[1]]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--target_file')
    args = parser.parse_args()
    closest_coords(args.target_file)