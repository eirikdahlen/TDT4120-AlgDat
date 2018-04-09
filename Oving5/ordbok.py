# Løsning vha tupler

def bygg(ordliste):
    rot = ({}, [])
    for word, pos in ordliste:
        trav_node = rot
        for char in word:
            if char not in trav_node[0]:
                trav_node[0][char] = ({}, [])
            trav_node = trav_node[0][char]
        trav_node[1].append(pos)
    return rot

def posisjoner(ord, indeks, node, lengde):
    char = ord[indeks]
    end = (indeks == lengde - 1)
    if char in node[0]:
        if end:
            return node[0][char][1]
        return posisjoner(ord, indeks + 1, node[0][char], lengde)
    elif char == '?':
        res = []
        for key in node[0]:
            if end:
                res += node[0][key][1]
            else:
                res += posisjoner(ord, indeks + 1, node[0][key], lengde)
        return res
    return []


def main():
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
        print(sokeord + ":", end ='')
        lengde = len(sokeord)
        posi = posisjoner(sokeord, 0, toppnode, lengde)
        posi.sort()
        for p in posi:
            print(" %s" % p, end='')
        print()
main()
