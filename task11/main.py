from typing import List
import doctest


def find_trading_cycle(preferences: List[List[int]]):

    cycle = []
    current_person = 0
    while current_person not in cycle:  # we will stop when we get someone that we already visited
        cycle.append(current_person)
        current_person = preferences[current_person][0]  # take their first priority
    cycle.append(current_person)  # close the cycle if the same person
    # use slice to begin the array from the person we just ended with
    cycle = cycle[cycle.index(current_person):]
    # print(cycle)  # print out the cycle
    return cycle


def top_trading_cycle(preferences: List[List[int]]):
    """
    >>> top_trading_cycle([[4,2,1,0,3,5],[5,3,1,0,4,2],[1,2,4,0,3,5],[2,5,1,0,3,4],[2,3,1,0,4,5],[3,4,1,0,2,5]])
    [[2, 1], [1, 5], [5, 3], [3, 2], [0, 4], [4, 0]]
    >>> top_trading_cycle([[1,2,3,0,4,5],[2,0,1,5,3,4],[3,0,2,1,4,5],[0,4,1,2,3,5],[4,0,1,3,2,5],[5,1,2,3,4,0]])
    [[0, 1], [1, 2], [2, 3], [3, 0], [4, 4], [5, 5]]
    >>> top_trading_cycle([[5,1,2,4,3,0],[1,5,2,3,0,4],[0,2,5,1,3,4],[5,3,4,1,2,0],[2,4,0,1,3,5],[4,2,1,3,0,5]])
    [[0, 5], [5, 4], [4, 2], [2, 0], [1, 1], [3, 3]]
    """
    answers = []  # keep the answers
    while len(answers) != len(preferences):  # while we still have unvisited "houses"
        cycle = find_trading_cycle(preferences)
        for i in range(len(cycle)-1):
            answers.append([cycle[i], cycle[i+1]])  # add this answer to the answers list
            for preference in preferences:
                preference.remove(cycle[i])  # remove all appearances of this house from all prefernces
    return answers



if __name__ == "__main__":
    doctest.testmod()
    # print out the answer in a clear way
    pref = [[4, 2, 1, 0, 3, 5], [5, 3, 1, 0, 4, 2], [1, 2, 4, 0, 3, 5], [2, 5, 1, 0, 3, 4], [2, 3, 1, 0, 4, 5], [3, 4, 1, 0, 2, 5]]
    ans = top_trading_cycle(pref)
    print(ans)
    for update in ans:
        print("player number", update[0], "get house number", update[1])