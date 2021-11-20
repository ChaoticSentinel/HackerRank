#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'hurdleRace' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY height
#


def hurdleRace(k, height):
    required_potion_sips = max([h - k for h in height])
    return required_potion_sips if required_potion_sips > 0 else 0


if __name__ == "__main__":
    k = 4
    height = [ 1, 6, 3, 5, 2 ]
    print(hurdleRace(k, height))
