#!/bin/env python3
import sys
import timeit
from collections import deque


def should_be_fast_as_fk():
    print("Hello World!")


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

    # def output(self):
    #     for conn in self.componentes():
    #         if conn.__len__() != 0:
    #             conn.sort()
    #             print(" ".join([str(x + 1) for x in conn]))


def main():
    graph = Graph()
    graph.output()


if __name__ == "__main__":
    main()
    # time = timeit.timeit(main)
    # print(time)
