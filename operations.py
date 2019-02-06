import math


def euclidean_dist(coord1: list, coord2: list):
    summ = 0
    for c1, c2 in zip(coord1, coord2):
        summ += (c1 - c2) ** 2

    return math.sqrt(summ)

