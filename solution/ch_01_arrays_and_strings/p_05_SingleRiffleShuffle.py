"""
Problem: Write a function to tell us if a full deck of cards shuffled_deck
is a single riffle of two other halves half1 and half2.
"""
import random


def solution_is_riffle_shuffle(half_a, half_b, deck):
    """
    Checks if a deck is the product of a riffle shuffle of two known halves

    >>> solution_is_riffle_shuffle([1, 3], [2, 4], [1, 2, 3, 4])
    True
    """
    if len(deck) != (len(half_a) + len(half_b)):
        return False

    a = 0
    b = 0

    for c in deck:
        if a < len(half_a) and c == half_a[a]:
            a += 1
        elif b < len(half_b) and c == half_b[b]:
            b += 1
        else:
            return False
    return True


def get_deck():
    return list(range(1, 53))


def riffle_shuffle(half_a, half_b):
    deck_size = (len(half_a) + len(half_b))
    shuffled = [None] * (deck_size)

    # Indicies for the halves
    a = 0
    b = 0

    for i in range(deck_size):
        if a >= len(half_a):
            shuffled[i] = half_b[b]
            b += 1
        elif b >= len(half_b):
            shuffled[i] = half_a[a]
            a += 1
        else:
            is_from_half_a = bool(random.getrandbits(1))

            if is_from_half_a:
                shuffled[i] = half_a[a]
                a += 1
            else:
                shuffled[i] = half_b[b]
                b += 1

    return shuffled
