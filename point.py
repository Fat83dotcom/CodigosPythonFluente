from math import hypot


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.__x = x
        self.__y = y

    @property
    def x(self) -> float:
        return self.__x

    @property
    def y(self) -> float:
        return self.__y

    def __abs__(self):
        '''Representa a distancia entre pontos'''
        return round(hypot(self.x, self.y), 2)

    def __repr__(self) -> str:
        return f'Point({self.x}, {self.y})'

    def __sub__(self, other: float):
        return Point((self.x - other.x), (self.y - other.y))

    def distance(self, pOther) -> float:
        return abs((self - pOther))


if __name__ == '__main__':

    a = Point(2.2, 2.5)
    b = Point(2, 2)

    c = a.distance(b)
    print(c)

    print(abs(a))
    print(abs(b))
