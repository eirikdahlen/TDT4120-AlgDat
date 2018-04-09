#!/usr/bin/python3

from sys import stdin
from itertools import repeat

def merge(decks):
    result = split(decks)

    string = ""
    for i in range(len(result)):
        string += result[i][1]
    return string

def split(list):
    if len(list) < 2: return list[0]

    mid = len(list)//2
    leftDeck = split(list[:mid])
    rightDeck = split(list[mid:])

    return merge_2(leftDeck, rightDeck)

def merge_2(leftDeck, rightDeck):
    result = []
    i, j = 0, 0

    while len(leftDeck) > i and len(rightDeck) > j:
        if leftDeck[i] > rightDeck[j]:
            result.append(rightDeck[j])
            j += 1
        else:
            result.append(leftDeck[i])
            i += 1

    while len(leftDeck) > i:
        result.append(leftDeck[i])
        i += 1
    while len(rightDeck) > j:
        result.append(rightDeck[j])
        j += 1

    return result


def main():

    decks = []

    for line in stdin:
        (index, csv) = line.strip().split(':')
        deck = list(zip(map(int, csv.split(',')), repeat(index)))
        decks.append(deck)

    print(merge(decks))


if __name__ == "__main__":
    main()
