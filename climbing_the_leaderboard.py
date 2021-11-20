#!/usr/bin/env python

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#


def find_scores_placement(leaderboard_ranking, play):
    length = len(leaderboard_ranking) - 1
    return find_scores_placement_recurse(leaderboard_ranking, play, 0, length) + 1


def find_scores_placement_recurse(leaderboard_ranking, play, start, end):
    if start > end:
        return end + 1
    mid = (end + start) // 2
    if play == leaderboard_ranking[mid]:
        return mid
    elif play > leaderboard_ranking[mid]:
        return find_scores_placement_recurse(leaderboard_ranking, play, start, mid - 1)
    else:
        return find_scores_placement_recurse(leaderboard_ranking, play, mid + 1, end)


def climbingLeaderboard(leaderboard, plays):
    leaderboard_ranking = sorted(set(leaderboard), reverse=True)
    first_place_score = leaderboard_ranking[0]
    last_place_score = leaderboard_ranking[-1]
    last_place_rank = len(leaderboard_ranking) + 1
    seen_scores = dict()

    play_rankings = []
    for i, play in enumerate(plays):
        if play in seen_scores:
            play_rankings.append(seen_scores[play])
            continue
        if play > first_place_score:
            play_rankings.append(1)
            continue
        if play < last_place_score:
            play_rankings.append(last_place_rank)
            continue

        score = find_scores_placement(leaderboard_ranking, play)
        seen_scores[play] = score
        play_rankings.append(score)
    return play_rankings


if __name__ == "__main__":
    ranked = [100, 90, 90, 80, 75, 60]
    player = [50, 65, 77, 90, 102]
    print(climbingLeaderboard(ranked, player))
