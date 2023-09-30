from point import Point


class Rectangle:
    def __init__(
        self, height: float, width: float, mainCorner: Point
    ) -> None:
        self.__height = height
        self.__width = width
        self.__corner = mainCorner

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    @property
    def corner(self):
        return self.__corner

    def getAllPoints(self) -> list:
        pA = self.corner
        pB = Point((self.corner.x + self.width), self.corner.y)
        pC = Point(
            (self.corner.x + self.width), (self.corner.y + self.height)
        )
        pD = Point((self.corner.x), (self.corner.y + self.height))
        return [pA, pB, pC, pD]


if __name__ == '__main__':

    p = Point(3, 3)
    r = Rectangle(3, 4, p)
    print(r.getAllPoints())
