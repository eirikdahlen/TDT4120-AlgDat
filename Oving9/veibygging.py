from sys import stdin

Inf = float(1e3000)

def mst(nm):
    maxEdge = 0
    nodes = set()
    weights = []
    for k in range(0, len(nm[0])):
        nodes.add(k)
        weights.append(Inf)
    lastNode = 0
    for i in range(0, len(nm[0]) - 1):
        nodes.remove(lastNode)
        minEdge = Inf
        minNode = 0
        for j in nodes:
            if nm[lastNode][j] < weights[j]:
                weights[j] = nm[lastNode][j]
            if weights[j] < minEdge:
                minEdge = weights[j]
                minNode = j
        lastNode = minNode
        if weights[lastNode] > maxEdge:
            maxEdge = weights[lastNode]
    return maxEdge


lines = []
for str in stdin:
    lines.append(str)
n = len(lines)
neighbour_matrix = [None] * n
node = 0
for line in lines:
    neighbour_matrix[node] = [Inf] * n
    for k in line.split():
        data = k.split(':')
        neighbour = int(data[0])
        weight = int(data[1])
        neighbour_matrix[node][neighbour] = weight
    node += 1
print (mst(neighbour_matrix))
