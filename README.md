# Exercise

Your task is to create a Java/Python program which reads a text file where each line contains the coordinates of a multidimensional point, and then looks for the closest pair of points in the file. If the program has found the closest pair of points, it should output the line numbers and the coordinates of the two closest points.

The text file contains one point per line. The coordinate values are separated by a tabulator character. The coordinate values are not necessarily integers. In case of a floating point coordinate value the decimal separator is a period.

## Requirements
Python 3.6+

## Getting Started

After cloning the repository:
```bash
git clone https://github.com/Koncsi/closest-coords.git
cd closest-coords
```

To find the two closest point in the dataset use the following command:
```bash
python closest_coords.py --target_file <file_path>
# save results to file:
python closest_coords.py --target_file <file_path> > <out_file.txt>
```

To run a simple benchmark, run the following:
```bash
python benchmark.py --directory <dir_path> --sample_number
python benchmark.py --directory <dir_path> --dim_depth
```
You can test for sample size increase or coordinate dimension increase.

## Summary

The program have three main parts. The data reading, the distance function and the search algorithm.Additionally, I created a simple benchmark and a data generator class to show the weakness of the current implementation.

The data reader function is a simple one thread implementation with the built-in tools.

The Eucledian distance function iteration through the given coordinates. The running time is depends on the dimensionality of the coordinates. It means that this function has _O(n)_ asymptotical running time, where _n_ is the coordinate's dimension.

The search algorithm compares each coordinate to every other coordinate. It means that in theory the running time of the algorithm is _O(n**2)_ where _n_ is the number of the coordinates.

To check the theoretical assumptions, I created the data generator and the benchmarks.

With an _O(n**2)_ algorithm the program can only work with fewer sample size. To address that issue, we can use for example Numba, to optimize our algorithm for more efficient hardware usage. Or we have to come up with a totally different approach. Problems like this can be "easily" fit to a GPU. 



## Results:

The following results were generated with CPU on 4.2GHz using a single thread.

To test the sample size dependence, 10 dimensional coordinates were used. Every test run three times.

| Target | Mean duration |
| ---- | --- |
| **100 samples** | 0.013 s|
| **1000 samples** | 1.275 s |
| **10000 samples** | 129 s |

As expected, 10x increase in sample size resulted 100x duration increase.


To test the coordinate dimensionality dependence, 100 samples were used. Every test run three times.

| Target | Mean duration |
| ---- | --- |
| **100 dimensions** | 0.092 s|
| **1000 dimensions** | 0.89 s |
| **10000 dimensions** | 8.8 s |

As expected, 10x increase in dimension size resulted 10x increase in duration.
