#!/usr/bin/env python3


def equalizeArray(arr):
    occurance_count = dict()
    for i in arr:
        if i in occurance_count:
            occurance_count[i] += 1
        else:
            occurance_count[i] = 1
    most_occuring = max(occurance_count, key=occurance_count.get)
    return sum([v for (k,v) in occurance_count.items() if k != most_occuring])


if __name__ == "__main__":
    arr = [1, 2, 2, 2, 3, 4, 5]
    print(equalizeArray(arr))
