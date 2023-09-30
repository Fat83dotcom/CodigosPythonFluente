from point import Point
from rectangle import Rectangle


class Circle:
    def __init__(self, center: Point, radius: float) -> None:
        self.__center = center
        self.__radius = radius

    @property
    def center(self):
        return self.__center

    @property
    def radius(self):
        return self.__radius

    def __repr__(self) -> str:
        return f'Circle({self.center}, {self.radius})'

    def inCircle(self, p: Point) -> bool:
        if self.center.distance(p) <= self.radius:
            return True
        return False

    def rectangleInCircle(self, recta: Rectangle):
        for p in recta.getAllPoints():
            if not self.center.distance(p) <= self.radius:
                return False
        return True


if __name__ == '__main__':

    p = Point(3, 3)

    pR = Point(4, 6)

    r = Rectangle(2, 3, p)

    G = Point(7.75, 4.36)
    F = Point(4.93, 4.71)
    H = Point(-4.5, 5.6)
    II = Point(-4.8, -4.19)
    J = Point(-0.25, -0.23)
    K = Point(-1.99, 3.28)

    c = Circle(p, 5)

    print(f'O quadrado esta contido no circulo: {c.rectangleInCircle(r)}')

    print(f'O ponto está contido no circulo: {c.inCircle(G)}')
    print(f'O ponto está contido no circulo: {c.inCircle(F)}')
    print(f'O ponto está contido no circulo: {c.inCircle(H)}')
    print(f'O ponto está contido no circulo: {c.inCircle(II)}')
    print(f'O ponto está contido no circulo: {c.inCircle(J)}')
    print(f'O ponto está contido no circulo: {c.inCircle(K)}')

    # print(c)
