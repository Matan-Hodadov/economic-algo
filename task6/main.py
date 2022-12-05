from typing import List
import doctest
import networkx as nx


# NOTICE: this function check if the graph is CYCLE FREE
def find_cycle_in_consumption_graph(divisions_matrix: List[list]) -> list:
    """
    tests
    >>> find_cycle_in_consumption_graph([[1, 1, 0.07, 0], [0, 0, 0.93, 1]])
    []
    >>> find_cycle_in_consumption_graph([[0, 0, 0.93, 1], [1, 1, 0.07, 0]])
    []
    >>> find_cycle_in_consumption_graph([[1, 1, 0.07, 0], [0.0, 0, 0, 0], [0, 0, 0.93, 1]])
    []
    >>> find_cycle_in_consumption_graph([[1, 0.4, 0.07, 0], [0, 0.6, 0.93, 1]])
    [(0, 3), (3, 1), (1, 4), (4, 0)]
    >>> find_cycle_in_consumption_graph([[0, 0.6, 0.93, 1], [1, 0.4, 0.07, 0]])
    [(0, 3), (3, 1), (1, 4), (4, 0)]
    >>> find_cycle_in_consumption_graph([[0, 0, 0, 0], [1, 0.4, 0.07, 0], [0, 0.6, 0.93, 1]])
    [(1, 4), (4, 2), (2, 5), (5, 1)]
    >>> find_cycle_in_consumption_graph([[0.2, 0.2, 0.2], [0.8, 0., 0.8], [0, 0.2, 0.0]])
    [(0, 3), (3, 1), (1, 5), (5, 0)]
    """
    m = len(divisions_matrix)  # number of players
    n = len(divisions_matrix[0])  # number of items

    G = nx.Graph()  # create the graph using networkx (nx)
    # go through each value in the matrix
    for player_index in range(m):
        for item_division_index in range(n):
            if divisions_matrix[player_index][item_division_index] > 0:  # if there is an edge
                G.add_edge(player_index, m + item_division_index)  # add this edge in our graph

    # using try in order to use find_cycle to find simple cycle in our graph
    try:  # try to use find_cycle
        any_cycle = nx.find_cycle(G)
    except:  # if there is no cycle make any_cycle equal to []
        any_cycle = []
    finally:  # regardless to the try except return the value inside any_cycle
        return any_cycle


if __name__ == '__main__':
    doctest.testmod()

