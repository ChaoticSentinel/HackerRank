#!/usr/bin/env python3


def repeatedString(s, n):
    return s.count("a") * (n // len(s)) + s[: n % len(s)].count("a")


if __name__ == "__main__":
    s = "abcdsasdfasaa"
    n = 5000
    print(repeatedString(s, n))
