class Coord:
    def __init__(self, x: int, y: int):
        self._c = (x,y)

    def __repr__(self) -> str:
        return "(%d, %d)" % (self.x, self.y)

    @property
    def x(self):
        return self._c[0]

    @property
    def y(self):
        return self._c[1]

    def __add__(self, other):
        return Coord(self.x+other.x, self.y+other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash(self._c)

    def __str__(self):
        return str(self._c)
