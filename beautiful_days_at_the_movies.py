#!/usr/bin/env python

#
# Complete the 'beautifulDays' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER i
#  2. INTEGER j
#  3. INTEGER k
#


def beautifulDays(i, j, k):
    dumb_game = [abs(i - int(str(i)[::-1])) for i in range(i, j + 1)]
    return len([1 for r in dumb_game if r % k == 0])


if __name__ == "__main__":
    i = 20
    j = 23
    k = 6
    print(beautifulDays(i, j, k))
