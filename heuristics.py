# coding=utf-8
from random import randint
import games


def memoize(f):
    memo = {}

    def helper(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]

    return helper


# Heurística aleatoria
def get_random_move(state):
    return randint(-100, 100)


def get_winning_alignments(state):
    pass


def get_losing_alignments(state):
    pass


@memoize
def get_move(state):
    return get_winning_alignments(state) - get_losing_alignments(state)
