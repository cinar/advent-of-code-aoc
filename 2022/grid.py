from collections import namedtuple
import math


class Grid:
    def __init__(self, cells, cols):
        self._cells = list(cells)
        self._cols = cols

    def __repr__(self):
        return "\n".join(
            [
                "".join(self._cells[i : i + self._cols])
                for i in range(0, len(self._cells), self._cols)
            ]
        )

    def cols(self):
        """Returns the number of grid columns."""
        return self._cols

    def rows(self):
        """Returns the number of grid rows."""
        return len(self._cells) // self._cols

    def size(self):
        """Returns the grid size."""
        return self.rows() * self.cols()

    def is_valid_row(self, row):
        """Checks if given row is a valid row."""
        return row >= 0 and row < self.rows()

    def is_valid_col(self, col):
        """Checks if given col is a valid col."""
        return col >= 0 and col < self._cols

    def is_valid_pos(self, pos):
        """Checks if valid pos."""
        return self.is_valid_row(pos[0]) and self.is_valid_col(pos[1])

    def is_valid_index(self, index):
        """Checks if valid index."""
        return index >= 0 and index < len(self._cells)

    def find_index_of(self, value):
        """Finds the index of given value."""
        return self._cells.index(value)

    def find_index_of_all(self, value):
        """Find all index of given value."""
        return [i for i, v in enumerate(self._cells) if v == value]

    def index_to_pos(self, index):
        """Translate index to pos."""
        return divmod(index, self._cols)

    def pos_to_index(self, row, col):
        """Translate pos to index."""
        return (row * self._cols) + col

    def north_of(self, index):
        """North of given index."""
        return index - self._cols

    def south_of(self, index):
        """South of given index."""
        return index + self._cols

    def west_of(self, index):
        """West of given index."""
        return index - 1

    def east_of(self, index):
        """East of given index."""
        return index + 1

    def orthogonal_neighbours(self, index):
        """Orthogonal neighbours of index."""
        return [
            n
            for n in [
                self.north_of(index),
                self.south_of(index),
                self.west_of(index),
                self.east_of(index),
            ]
            if self.is_valid_index(n)
        ]

    def at_index(self, index):
        """At index."""
        return self._cells[index]

    def set_index(self, index, value):
        """Set index."""
        self._cells[index] = value

    def distance(self, pos1, pos2):
        """Distance between two positions."""
        return math.sqrt(
            math.pow(pos2[0] - pos1[0], 2) + math.pow(pos2[1] - pos1[1], 2)
        )

    def distance_to_index(self, index, neighbours):
        """Distance from neighbours to given index."""
        pos2 = self.index_to_pos(index)
        return [(self.distance(self.index_to_pos(n), pos2), n) for n in neighbours]
