from state import *
from heapq import *
from pair import *
import time
import os

class Astar:
    def __init__(self):
        self.path = []
        self.steps = 0

    def search(self, start_field):
        start = State(start_field, 0, None)
        unvisited = []
        visited = set()
        f = start.g + get_heuristic(start)
        heappush(unvisited, Pair(f, start))
        while len(unvisited) != 0:
            curr = heappop(unvisited)
            if curr.state.field == TARGET:
                return curr.state
            visited.add(tuple(curr.state.field))
            for v in curr.state.get_moves():
                if (tuple(v) in visited):
                    continue
                else:
                    v_g = curr.state.g + 1
                    obj = find_state(unvisited, v)
                    is_better = False
                    if obj:
                        if v_g < obj.state.g:
                            unvisited.remove(obj)
                            is_better = True
                    else:
                        is_better = True
                    if is_better:
                        new_state = State(v, v_g, curr.state)
                        f_new = new_state.g + get_heuristic(new_state)
                        heappush(unvisited, Pair(f_new, new_state))
        return None

    def print_path(self, state, slp=1):
        while not state is None:
            self.path.append(state)
            state = state.parent

        self.path.reverse()
        self.steps = len(self.path)

        for st in self.path:
            time.sleep(slp)
            print_matrix(st)

        print("NUMBER OF STEPS: ", self.steps)

#------------------------Astar end----------------------------------------------
def find_state(q, s):
    for e in q:
        if e.state.field == s:
            return e
    return None


def print_matrix(state):
    for i in range(len(state.field)):
        if i % 4 == 0:
            print('\n')
        print('{0:2d}'.format(state.field[i]), " ", end='')
    print('\n')
