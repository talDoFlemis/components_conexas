#!/bin/env python3
import sys


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
        self.edges = edges

    def neighbors(self, v):
        return [x for x in self.adj[v] if x != 0]

    def usguri(self):
        for i in range(self.adj.__len__()):
            print(self.adj[i])


def main():
    graph = Graph()
    graph.usguri()


if __name__ == "__main__":
    main()
