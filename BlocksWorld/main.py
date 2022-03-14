from BlocksWorld import BlocksWorld

import string
import random


test = BlocksWorld()

stacks = int(input("Eisagete arithmo stoivwn: "))
blocks = int(input("Eisagete arithmo block: "))


def startState(stacks, blocks):
    ls = stacks
    b = list(string.ascii_uppercase)  # string.digits
    blocks_list = b[:blocks]
    random.shuffle(blocks_list)

    problem_state = []
    while blocks:
        if not blocks_list: break

        if stacks == 1:
            problem_state.append(blocks_list)
            break

        else:
            r = random.randint(1, blocks)
            s = blocks_list[:r]
            problem_state.append(s)

        blocks -= r
        stacks -= 1
        blocks_list = blocks_list[r:]
    while len(problem_state) < ls:
        problem_state += [[]]

    random.shuffle(problem_state)
    return problem_state


startSt = startState(stacks, blocks)


def goal_generator(startSt):
    goal = []
    for stack in startSt:
        goal += stack
    goal.sort()
    goal = [goal]

    for i in range(len(startSt) - 1):
        goal += [[]]
    return goal


goalSt = goal_generator(startSt)

print("Start State: ", startSt)
print("Goal State: ", goalSt)
print("Lysh: ", test.solve(startSt, goalSt))
