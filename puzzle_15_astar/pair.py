class Pair:
    def __init__(self, _cost, _state):
        self.cost = _cost
        self.state = _state


    def __copy__(self):
        new_pair = Pair(self.cost, self.state)
        return new_pair


    def __lt__(self, other):
        return self.cost < other.cost

    def __le__(self, other):
        return self.cost <= other.cost

    def __eq__(self, other):
        return self.get_field() == other.get_field()


    def get_field(self):
        return self.state.field
