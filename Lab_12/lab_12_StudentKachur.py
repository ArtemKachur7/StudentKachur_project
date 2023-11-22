import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_xy(self, x, y):
        return math.hypot(self.__x - x, self.__y - y)

    def distance_from_point(self, point):
        return self.distance_from_xy(point.getx(), point.gety())


class Triangle:
    def __init__(self, vertice1, vertice2, vertice3):
        self.__vertices = [vertice1, vertice2, vertice3]

    def perimeter(self):
        side1 = self.__vertices[0].distance_from_point(self.__vertices[1])# Обчислюємо довжини сторін трикутника
        side2 = self.__vertices[1].distance_from_point(self.__vertices[2])
        side3 = self.__vertices[2].distance_from_point(self.__vertices[0])
        return side1 + side2 + side3 # Повертаємо периметр трикутника

# Користувач вводить координати вершин трикутника
x1, y1 = map(float, input("Введіть координати вершини A (x, y) через пробіл: ").split())
x2, y2 = map(float, input("Введіть координати вершини B (x, y) через пробіл: ").split())
x3, y3 = map(float, input("Введіть координати вершини C (x, y) через пробіл: ").split())

PointA = Point(x1, y1)
PointB = Point(x2, y2)
PointC = Point(x3, y3)

triangle = Triangle(PointA, PointB, PointC)

print(f"Периметр трикутника із заданими сторонами : P={triangle.perimeter()}")