import itertools
from typing import List


def finding_egalitarian_division(possible_divisions: List) -> tuple:
    return possible_divisions[[min(x) for x in possible_divisions].index(max([min(x) for x in l]))]


def create_all_divisions(table: List) -> List:
    possible_divisions = [[0]*len(table)]
    for i in range(len(table[0])):
        column = [row[i] for row in table]
        new_divisions = []
        for previously_division in possible_divisions:
            for j in range(len(column)):
                temp = previously_division.copy()
                temp[j] += column[j]
                new_divisions.append(temp)
        possible_divisions = new_divisions
    return possible_divisions


def create_all_divisions_after_pruning(table: List) -> List:
    possible_divisions = [[0]*len(table)]
    for i in range(len(table[0])):
        column = [row[i] for row in table]
        new_divisions = []
        for previously_division in possible_divisions:
            for j in range(len(column)):
                temp = previously_division.copy()
                temp[j] += column[j]
                if temp not in new_divisions:
                    new_divisions.append(temp)
        possible_divisions = new_divisions
    return possible_divisions


if __name__ == '__main__':
    # create divisions
    items_eval = [12, 7, 10]
    table = [items_eval,
             items_eval]
    # table = [[11, 11, 55],
    #          [22, 22, 33],
    #          [33, 44, 0]]
    # table = [[11, 11], [22, 22], [33, 44]]
    all_divisions = create_all_divisions(table)
    print(all_divisions)

    l = all_divisions
    # l = [(1, 2, 3), (1, 2, 4), (5, 3, 2)]
    # # l = [[1, 2, 3], [1, 2, 4], [5, 3, 2]]
    b = finding_egalitarian_division(l)
    print(b)


    table = [[11, 11, 55],
             [22, 22, 33],
             [33, 44, 0]]
    print(len(create_all_divisions(table)))
    print(len(create_all_divisions_after_pruning(table)))

