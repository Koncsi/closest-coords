import time
import argparse

from data_tools import DataGenerator
from closest_coords import closest_coords

def benchmark_closest_cords(dir_path, test_samples):
    dg = DataGenerator(dir_path)

    if test_samples:
        sample1 = dg.generate_dataset(100, 10)
        sample2 = dg.generate_dataset(1000, 10)
        sample3 = dg.generate_dataset(10000, 10)

        start_time = time.time()
        closest_coords(sample1)
        duration1 = time.time() - start_time

        start_time = time.time()
        closest_coords(sample2)
        duration2 = time.time() - start_time

        start_time = time.time()
        closest_coords(sample3)
        duration3 = time.time() - start_time

        print(f'Dataset with 10 dimension and 100 samples run for: {duration1}')
        print(f'Dataset with 10 dimension and 1000 samples run for: {duration2}')
        print(f'Dataset with 10 dimension and 10000 samples run for: {duration3}')

    else:
        sample1 = dg.generate_dataset(100, 100)
        sample2 = dg.generate_dataset(100, 1000)
        sample3 = dg.generate_dataset(100, 10000)

        start_time = time.time()
        closest_coords(sample1)
        duration1 = time.time() - start_time

        start_time = time.time()
        closest_coords(sample2)
        duration2 = time.time() - start_time

        start_time = time.time()
        closest_coords(sample3)
        duration3 = time.time() - start_time

        print(f'Dataset with 100 dimension and 100 samples run for: {duration1}')
        print(f'Dataset with 1000 dimension and 100 samples run for: {duration2}')
        print(f'Dataset with 10000 dimension and 100 samples run for: {duration3}')


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--directory')
    parser.add_argument('--sample_number', dest='test_samples', action='store_true')
    parser.add_argument('--dim_depth', dest='test_samples', action='store_false')
    parser.set_defaults(test_samples=True)
    args = parser.parse_args()
    benchmark_closest_cords(args.directory, args.test_samples)