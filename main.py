#!/bin/env python3


class Graph:
    def __init__(self, filename):
        n = 0
        edges = []
        with open(filename, "r") as f:
            for i, line in enumerate(f):
                if i == 2:
                    n = int(line.split("=")[1])
                elif i >= 4:
                    edges.append([int(x) for x in line.split()])
        self.n = n
        self.edges = edges
        self.adj = [[1] for _ in range(n)]

    def output(self):
        print(self.n)
        for i in range(self.n):
            print(self.adj[i])


def main():
    graph = Graph("./exemplos/instancias/0.in")
    graph.output()


if __name__ == "__main__":
    main()
