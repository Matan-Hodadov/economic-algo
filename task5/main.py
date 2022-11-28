from typing import List
import doctest


# NOTICE: this function check if the graph is CYCLE FREE
def is_simple_cycle_free(divisions_matrix: List) -> bool:
    """
    tests
    >>> is_simple_cycle_free([[1, 1, 0.07, 0], [0, 0, 0.93, 1]])
    True
    >>> is_simple_cycle_free([[0, 0, 0.93, 1], [1, 1, 0.07, 0]])
    True
    >>> is_simple_cycle_free([[1, 1, 0.07, 0], [0.0, 0, 0, 0], [0, 0, 0.93, 1]])
    True
    >>> is_simple_cycle_free([[1, 0.4, 0.07, 0], [0, 0.6, 0.93, 1]])
    False
    >>> is_simple_cycle_free([[0, 0.6, 0.93, 1], [1, 0.4, 0.07, 0]])
    False
    >>> is_simple_cycle_free([[0, 0, 0, 0], [1, 0.4, 0.07, 0], [0, 0.6, 0.93, 1]])
    False
    """

    m = len(divisions_matrix)  # number of players
    n = len(divisions_matrix[0])  # number of items

    # take the sub-graph which contains only the players and the shared items (2 or more edges)

    # remove a player node if he doesn't have any edges
    empty_player_edge_list = [0 for i in range(n)]
    divisions_matrix = [edge_list for edge_list in divisions_matrix if edge_list != empty_player_edge_list]
    new_m = len(divisions_matrix)

    # "remove" items with only less the 2 edges (1 or 0)
    # we will use zip in order to move from representation of rows to columns
    new_n = n
    column_list = list(zip(*divisions_matrix))  # get list that each index is column respectively
                                                # first index is the first culomn and so on
    for col_index in range(n):  # for each column
        # create list which contains the values that bigger than 0 and check this list len
        edges_num = len([i for i in column_list[col_index] if i > 0])
        if edges_num < 2:  # if there are no more than 2 edges
            for player in divisions_matrix:
                player[col_index] = 0
            new_n -= 1

    # now after we removed the items with less the 2 edges we need to calculate total number of edges
    num_of_edges = 0
    for player in divisions_matrix:  # for each list (player) in our matrix (sub-graph)
        # if there is a value that is bigger than 0 this represents an edge in our graph
        # we create a list with those values and take the len of this list
        num_of_edges += len([i for i in player if i > 0])

    # now all we got to do is check if the number of edges is equal or bigger then the number of nodes
    return num_of_edges < (new_m + new_n)


if __name__ == '__main__':
    doctest.testmod()

    matrix = [[0.6, 1, 0.07, 0],
              [0.1, 0, 0.0, 0],
              [0.3, 0, 0.93, 1]]
    print("expected: False, got:", is_simple_cycle_free(matrix))


