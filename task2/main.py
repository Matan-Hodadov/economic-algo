from typing import List


class Agent:
    def __init__(self, values: List[int]):
        self.values = values

    def value(self, option: int) -> float:
        """
        INPUT:    the index of an option.
        OUTPUT:   the value of the option to the agent.
        """
        return self.values[option]


def isParetoImprovement(agents: List[Agent], option1: int, option2: int) -> bool:
    improvement_flag = False
    for agent in agents:
        difference = agent.value(option1) - agent.value(option2)
        if difference < 0:
            return False
        if not improvement_flag and difference > 0:
            improvement_flag = True
    return improvement_flag


def isParetoOptimal(agents: List[Agent], option: int, allOptions: List[int]) -> bool:
    for i in allOptions:
        if isParetoImprovement(agents, i, option):
            return False
    return True


if __name__ == '__main__':
    Ami = Agent([1, 2, 3, 4, 5])
    Tami = Agent([3, 1, 2, 5, 4])
    Rami = Agent([3, 5, 5, 1, 1])
    agents = [Ami, Tami, Rami]
    allOptions = [0, 1, 2, 3, 4]


    # print(isParetoImprovement(agents, 1, 2))
    print(isParetoOptimal(agents, 0, allOptions))
    print(isParetoOptimal(agents, 1, allOptions))
    print(isParetoOptimal(agents, 2, allOptions))
    print(isParetoOptimal(agents, 3, allOptions))
    print(isParetoOptimal(agents, 4, allOptions))


