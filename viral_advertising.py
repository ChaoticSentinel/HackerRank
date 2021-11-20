#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'viralAdvertising' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#

# n0: (5 // 2)
# n1: (n0 * 3) // 2
# n2: (n1 * 3) // 2
# n3: (n2 * 3) // 2


def viralAdvertising_recurse(n, c, previous_likes, total_likes):
    if c >= n:
        return total_likes
    if c == 0:
        return viralAdvertising_recurse(n, c + 1, (5 // 2), 2)
    new_likes = (previous_likes * 3) // 2
    return viralAdvertising_recurse(n, c + 1, new_likes, total_likes + new_likes)


def viralAdvertising(n):
    return viralAdvertising_recurse(n, 0, 0, 0)


if __name__ == "__main__":
    n = 5
    print(viralAdvertising(n))
