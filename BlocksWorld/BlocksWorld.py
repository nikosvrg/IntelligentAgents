import copy
import string
import random

class BlocksWorld:

    def __init__(self):
        pass

    def solve(self, start, goal):

        class State:
            def __init__(self, stack1, stack2, total, moves=None):
                if moves is None:
                    moves = []
                self.stack1 = stack1
                self.stack2 = stack2
                self.total= total
                self.moves = moves

            def __eq__(self, other):
                return (self.stack1 == other.stack1 and self.stack2 == other.stack2
                        and self.total == other.total and self.moves == other.moves)

            def goal_state_move(self):
                while self.difference() != 0:
                    self = self.select_move()
                return self.moves

            def select_move(self):  # tha epistrepsei thn kalyterh kinhsh
                #metakinisi teleutaiou block sthn stoiva
                #an den meiwthei h diafora, metakinisi sto trapezi
                for index, stack in enumerate(self.stack1):
                    for index2, stack2 in enumerate(self.stack1):
                        if index != index2:
                            curr_table, move = self.valid_state_move(self.stack1, index, index2)
                            new_state = State(curr_table, self.stack2, self.total, copy.copy(self.moves))
                            new_state.moves.append(move)
                            if new_state.difference() < self.difference():
                                return new_state

                # metakinisi teleutaiou block sto trapezi
                # an vrisketai sto trapezi skip
                for index, stack in enumerate(self.stack1):
                    if len(stack) > 1:
                        curr_table, move = self.valid_state_move(self.stack1, index, -1)  # -1 = trapezi
                        new_state = State(curr_table, self.stack2, self.total, copy.copy(self.moves))
                        new_state.moves.append(move)
                        if new_state.difference() <= self.difference():
                            return new_state

            def valid_state_move(self, table, start_index, end_index):
                temp_table = copy.deepcopy(table)
                left = temp_table[start_index]
                top_block = left.pop()
                right = []

                if end_index < 0:  # metakinisi sto trapezi (-1)
                    temp_table.append(right)
                    move = (top_block, 'Table')
                else:  # metakinisi stin stoiva
                    right = temp_table[end_index]
                    move = (top_block, right[-1])
                right.append(top_block)

                if len(left) == 0:
                    temp_table.remove(left)
                return temp_table, move

            def difference(self):
                same_num = 0
                # sygkrisi twn stoivwn
                for left in self.stack1:
                    for right in self.stack2:
                        index = 0
                        while index < len(left) and index < len(right):
                            if left[index] == right[index]:
                                same_num += 1
                                index += 1
                            else:
                                break
                diff = self.total - same_num
                return diff

        total = 0
        for l in start:
            for e in l:
                total += 1
        state = State(start, goal, total)
        solution = state.goal_state_move()

        return solution