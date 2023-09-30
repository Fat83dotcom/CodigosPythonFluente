class Vector:
    def __init__(self, x: float, y: float, z: float) -> None:
        self.__x = x
        self.__y = y
        self.__z = z

    def __add__(self, other):
        x = self.__x + other.x
        y = self.__y + other.y
        z = self.__z + other.z
        return Vector(x, y, z)

    def __sub__(self, other):
        x = self.__x - other.x
        y = self.__y - other.y
        z = self.__z - other.z
        return Vector(x, y, z)

    def escalar(self, k):
        return Vector(self.x * k, self.y * k, self.z * k)

    def __mul__(self, other) -> float:
        return (self.x * other.x) + (self.y * other.y) + (self.z * other.z)

    def __repr__(self) -> str:
        return f'Vector({self.__x}, {self.__y}, {self.__z})'

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def z(self):
        return self.__z


a = Vector(1, 2, 5)
b = Vector(2, -7, 12)

c: Vector = a * b

print(c)
