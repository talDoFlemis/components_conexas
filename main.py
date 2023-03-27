#!/bin/env python3
import sys
import timeit
from collections import deque


def merge(a, b):
    a.extend(x for x in b if x not in a)


def find(parents, a):
    root = a

    while parents[root] != root:
        parents[root] = parents[parents[root]]
        root = parents[root]
    return root


def union(parents, rank, a, b):
    pa, pb = find(parents, a), find(parents, b)

    if rank[pa] >= rank[pb]:
        parents[pb] = pa
        rank[pa] += rank[pb]
    else:
        parents[pa] = pb
        rank[pb] += rank[pa]


def should_be_fast():
    parents = []
    rank = []
    path = []
    n = 0
    for idx, line in enumerate(sys.stdin):
    # for idx, line in enumerate(open("./exemplos/instancias/0.in", "r")):
        if idx == 2:
            n = int(line.split("=")[1])
        if idx == 3:
            parents = [i for i in range(n)]
            path = [[] for _ in range(n)]
            rank = [1] * n
        elif idx >= 4:
            a, b = [int(x) for x in line.split()]
            union(parents, rank, a - 1, b - 1)

    for idx, el in enumerate(parents):
        if el == idx:
            path[idx].append(idx + 1)
            for i in range(n):
                if find(parents, i) == idx and i != idx:
                    path[idx].append(i + 1)
            path[idx].sort()

    path.sort()

    for p in path:
        if p.__len__() != 0:
            print(" ".join([str(x) for x in p]))


def find2(parents, a):
    root = a

    while parents[root][0] != root:
        parents[root][0] = parents[parents[root][0]][0]
        root = parents[root][0]
    return root


def union2(parents, rank, a, b):
    pa, pb = find2(parents, a), find2(parents, b)

    if rank[pa] >= rank[pb]:
        merge(parents[pa], parents[pb])
        parents[pb][0] = pa
        rank[pa] += rank[pb]
    else:
        merge(parents[pb], parents[pa])
        parents[pa][0] = pb
        rank[pb] += rank[pa]


def should_be_fast_2():
    parents = []
    rank = []
    n = 0
    for idx, line in enumerate(sys.stdin):
        if idx == 2:
            n = int(line.split("=")[1])
        if idx == 3:
            parents = [[i] for i in range(n)]
            rank = [1] * n
        elif idx >= 4:
            a, b = [int(x) for x in line.split()]
            union2(parents, rank, a - 1, b - 1)

    path = []

    for idx, el in enumerate(parents):
        if el[0] == idx:
            el.sort()
            path.append(el)

    path.sort()

    [print(" ".join([str(x + 1) for x in el])) for el in path]


class Graph:
    def __init__(self):
        n = 0
        for idx, line in enumerate(sys.stdin):
            if idx == 2:
                n = int(line.split("=")[1])
            if idx == 3:
                self.adj = [[0 for _ in range(n)] for _ in range(n)]
            elif idx >= 4:
                (a, b) = [int(x) for x in line.split()]
                self.adj[a - 1][b - 1] = self.adj[b - 1][a - 1] = 1
        self.n = n

    def neighbors(self, v):
        return [idx for idx, x in enumerate(self.adj[v]) if x != 0]

    def output(self):
        vis = [False for _ in range(self.n)]
        conn = [[] for _ in range(self.n)]

        for i in range(self.n):
            if not vis[i]:
                q = deque()
                q.append(i)
                vis[i] = True
                while len(q) != 0:
                    el = q.popleft()
                    conn[i].append(el)
                    for n in self.neighbors(el):
                        if not vis[n]:
                            vis[n] = True
                            q.append(n)

        for i in conn:
            if i.__len__() != 0:
                i.sort()
                print(" ".join([str(x + 1) for x in i]))


class Graph2:
    def __init__(self):
        n = 0
        self.adj = []
        for idx, line in enumerate(sys.stdin):
            if idx == 2:
                n = int(line.split("=")[1])
            if idx == 3:
                self.adj = [[] for _ in range(n)]
            elif idx >= 4:
                (a, b) = [int(x) for x in line.split()]
                self.adj[a - 1].append(b - 1)
                self.adj[b - 1].append(a - 1)
        self.n = n

    def dfs(self, temp, v, vis):
        vis[v] = True
        temp.append(v)

        for i in self.adj[v]:
            if not vis[i]:
                temp = self.dfs(temp, i, vis)
        return temp

    def output(self):
        vis = []
        conn = []
        for _ in range(self.n):
            vis.append(False)
        for v in range(self.n):
            if not vis[v]:
                temp = []
                conn.append(self.dfs(temp, v, vis))

        for i in conn:
            i.sort()
            print(" ".join([str(x + 1) for x in i]))


def main():
    # g = Graph2()
    # g.output()
    should_be_fast()
    # should_be_fast_2()
    # graph = Graph()
    # graph.output()


if __name__ == "__main__":
    main()
    # time = timeit.timeit(main)
    # print(time)
