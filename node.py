class Node:
    """
    A class for building nodes, the building blocks of linked structures.
    From section 3.21 of Problem Solving with Algorithms and Data Structures.
    """
    def __init__(self, init_data):
        self._data = init_data
        self._next = None

    def get_data(self):
        return self._data

    def get_next(self):
        return self._next

    def set_data(self, new_data):
        self._data = new_data

    def set_next(self, new_next):
        self._next = new_next

    def __repr__(self):
        return f'Node{self._data, self._next}'
