#!/usr/bin/env python3


def nonDivisibleSubset(k, s):
    remainder_counts = [0] * k
    for number in s:
        remainder_counts[number % k] += 1
    subset_size = min(remainder_counts[0], 1)
    for i in range(1, k // 2 + 1):
        if i != k - i:
            subset_size += max(remainder_counts[i], remainder_counts[k - i])
        else:
            subset_size += 1
    return subset_size


if __name__ == "__main__":
    k = 4
    s = [19, 10, 12, 10, 24, 25, 22]
    print(nonDivisibleSubset(k, s))
