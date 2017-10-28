import copy

SIZE = 4
TARGET = [1,2,3,4,
          5,6,7,8,
          9,10,11,12,
          13,14,15,0]

class State:
    def __init__(self, _field, _g, _p):
        self.g = _g
        self.parent = _p
        self.field = []
        for e in _field:
            self.field.append(e)


    def __eq__(self, other):
        return self.field == other.field


    def get_field(self):
        return self.field


    def __copy__(self):
        new = State([], self.g, self.parent)
        for e in self.field:
            new.field.append(e)
        return new


    def get_moves(self):
        m = copy.deepcopy(self.field)
        output = []

        i = m.index(0)

        if i // SIZE > 0:
            m[i], m[i - SIZE] = m[i - SIZE], m[i]
            output.append(copy.deepcopy(m))
            m[i], m[i - SIZE] = m[i - SIZE], m[i]

        if i // SIZE < 3:
          m[i], m[i + SIZE] = m[i + SIZE], m[i]
          output.append(copy.deepcopy(m))
          m[i], m[i + SIZE] = m[i + SIZE], m[i]

        if i % SIZE > 0:
          m[i], m[i - 1] = m[i - 1], m[i]
          output.append(copy.deepcopy(m))
          m[i], m[i - 1] = m[i - 1], m[i]

        if i % SIZE < 3:
          m[i], m[i + 1] = m[i + 1], m[i]
          output.append(copy.deepcopy(m))
          m[i], m[i + 1] = m[i + 1], m[i]

        return output


    def is_target(self):
        return self.field == TARGET

#-----------------------------State end-----------------------------------------

def get_heuristic(state):
    md = manhattan_dist(state)
    mt = misplaced_tiles(state)
    lvc = linear_vertical_conflict(state)
    lhc = linear_horizontal_conflict(state)
    return md + mt + lvc + lhc


def manhattan_dist(state):
    distance = 0
    for e in range(1, len(TARGET)):
        coord1 = state.field.index(e)
        coord2 = TARGET.index(e)
        distance += abs((coord1 % SIZE) - (coord2 % SIZE)) + abs((coord1 // SIZE) - (coord2 // SIZE))
    return distance

def misplaced_tiles(state):
    misplaced = 0
    compare = 0
    for i in range(1, 16):
        if state.field.index(i) != compare:
            misplaced += 1
        compare += 1
    if state.field.index(0) != 15:
        misplaced += 1
    return misplaced

def linear_vertical_conflict(state):
    conflict = 0
    m = -1
    row = 0
    for i in range(0, 16):
        if i // SIZE != row:
            m = -1
            row += 1
        val = state.field[i]
        if val != 0 and ((val - 1) // SIZE) == row:
            if val > m:
                m = val
            else:
                conflict += 2
    return conflict

def linear_horizontal_conflict(state):
    conflict = 0
    m = -1
    col = 0
    for i in range(0, 16):
        if i % SIZE != col:
            m = -1
            col += 1
        val = state.field[i]
        if val != 0 and (val - 1) % SIZE == col:
            if val > m:
                m = val
            else:
                conflict += 2
    return conflict
