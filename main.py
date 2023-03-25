#!/bin/env python3
import sys
import bisect
from queue import Queue


class Graph:
    def __init__(self):
        n = 0
        edges = []
        for idx, line in enumerate(sys.stdin):
            if idx == 2:
                n = int(line.split("=")[1])
            elif idx >= 4:
                edges.append([int(x) for x in line.split()])
        self.adj = [[0 for _ in range(n)] for _ in range(n)]
        for edge in edges:
            self.adj[edge[0] - 1][edge[1] - 1] = 1
            self.adj[edge[1] - 1][edge[0] - 1] = 1

    def neighbors(self, v):
        return [idx for idx, x in enumerate(self.adj[v]) if x != 0]

    def componentes(self):
        vis = [False for _ in range(self.adj.__len__())]
        conn = [[] for _ in range(self.adj.__len__())]

        for i in range(self.adj.__len__()):
            if not vis[i]:
                q = Queue()
                q.put(i)
                vis[i] = True
                while not q.empty():
                    el = q.get()
                    bisect.insort(conn[i], el)

                    for n in self.neighbors(el):
                        if not vis[n]:
                            vis[n] = True
                            q.put(n)

        return conn

    def output(self):
        for conn in self.componentes():
            if conn.__len__() != 0:
                print(" ".join([str(x + 1) for x in conn]))


def main():
    graph = Graph()
    graph.output()


if __name__ == "__main__":
    main()
