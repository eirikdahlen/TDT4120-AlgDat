#!/usr/bin/python3
from timeit import default_timer as timer


class Node:
    def __init__(self):
        self.barn = {}
        self.posi = []


def bygg(ordliste):
    rot = Node()
    for word, pos in ordliste:
        trav_node = rot
        for char in word:
            if char not in trav_node.barn:
                trav_node.barn[char] = Node()
            trav_node = trav_node.barn[char]
        trav_node.posi.append(pos)
    return rot

def posisjoner(ord, indeks, node, lengde):
    char = ord[indeks]
    end = (indeks == lengde - 1)
    if char in node.barn:
        if end:
            return node.barn[char].posi
        return posisjoner(ord, indeks + 1, node.barn[char], lengde)
    elif char == '?':
        res = []
        for key in node.barn:
            if end:
                res += node.barn[key].posi
            else:
                res += posisjoner(ord, indeks + 1, node.barn[key], lengde)
        return res
    return []

start = timer()
from sys import stdin
ord = stdin.readline().split()
ordliste = []
pos = 0
for o in ord:
    ordliste.append((o, pos))
    pos += len(o) + 1
toppnode = bygg(ordliste)
for sokeord in stdin:
    sokeord = sokeord.strip()
    print("%s:" % sokeord, end='')
    lengde = len(sokeord)
    posi = posisjoner(sokeord, 0, toppnode, lengde)
    posi.sort()
    for p in posi:
        print(" %s" % p, end='')
    print()
end = timer()
print(end-start)
