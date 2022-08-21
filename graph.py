NO_EDGE = 0
DEFAULT_EDGE_WEIGHT = 1 

class GraphAdjMatrix:
    def __init__(self, N_vertices):
        self.N_vertices = N_vertices
        self.adj_matrix = [[NO_EDGE for i in range(N_vertices)] for i in range(N_vertices)] 

    def add_edge(self, u, j):
        assert u < self.N_vertices 
        assert j < self.N_vertices 

        self.adj_matrix[u][j] = DEFAULT_EDGE_WEIGHT
        self.adj_matrix[j][u] = DEFAULT_EDGE_WEIGHT

    def get_all_edges(self):
        edges = []
        for i in range(self.N_vertices):
            for j in range(self.N_vertices):
                if self.adj_matrix[i][j] != NO_EDGE:
                    edges.append((i, j, self.adj_matrix[i][j]))

        return edges

    def bfs(self, root):
        visited, queue, order = [False for i in range(self.N_vertices + 1)], [root], []

        visited[root] = True
        while queue:
            curr = queue.pop(0)
            order.append(curr)

            for neighbor_vertex in self.get_neighbors(curr):
                if visited[neighbor_vertex] == False:
                    queue.append(neighbor_vertex)
                    visited[neighbor_vertex] = True

        return order

    def dfs(self, root):
        visited, stack, order = [False for i in range(self.N_vertices + 1)], [root], []

        visited[root] = True
        while stack:
            curr = stack.pop()
            order.append(curr)

            for neighbor_vertex in self.get_neighbors(curr):
                if visited[neighbor_vertex] == False:
                    stack.append(neighbor_vertex)
                    visited[neighbor_vertex] = True

        return order


    # this smells like a list comprehension oneliner but i could not get the index in thru enumerate and filter() :x
    # or we could just save neighbors directly instead of NxN matrix, but this is a Graph__AdjMatrix__ :)
    def get_neighbors(self, target):
        edges = []
        for i in range(self.N_vertices):
            if self.adj_matrix[target][i] != NO_EDGE:
                edges.append(i)

        return edges

def make_graph():
    g = GraphAdjMatrix(5)
    g.add_edge(1, 2)
    g.add_edge(0, 3)
    g.add_edge(0, 4)
    g.add_edge(4, 2)

    return g

import unittest

class TestGraphAdjMatrix(unittest.TestCase):
    def test_neighbors_0(self):
        self.assertEqual(make_graph().get_neighbors(0), [3, 4])

    def test_neighbors_2(self):
        self.assertEqual(make_graph().get_neighbors(2), [1, 4])

    def test_bfs_0(self):
        self.assertEqual(make_graph().bfs(0), [0, 3, 4, 2, 1])

    def test_dfs_0(self):
        self.assertEqual(make_graph().dfs(0), [0, 4, 2, 1, 3])
