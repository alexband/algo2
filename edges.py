#! -*- coding: utf-8 -*-
import heapq
from unionfind import UnionFind

class Edge(object):
    def __init__(self, node1, node2, cost=0, marked=None):
        self.node1 = node1
        self.node2 = node2
        self.cost = cost
        self.marked = marked

    def __cmp__(self, y):
        return self.cost - y.cost
    
    def __repr__(self):
        return '<Edge(%s, %s), cost:%s>' % (self.node1, self.node2, self.cost)

f = open('./edges.txt', 'r')
n_nodes, n2 = f.readline().strip().split()
edges = []
for l in f:
    a, b, c = l.split()
    edges.append(Edge(str(a), str(b), cost=int(c)))
edges = sorted(edges, key=lambda x: x.cost)
U = UnionFind()
T = []
for e in edges:
    if U[e.node1] != U[e.node2]:
        T.append(e)
        U.union(e.node1, e.node2)
print sum(e.cost for e in T)


