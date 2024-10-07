class Figure:
    unit = 'cm'

    def __init__(self):
        pass

    def calculate_area(self):
        raise

    def info(self):
        raise

class Sguare(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        area = self.calculate_area()
        print(f"Длина стороны квадрата: {self.__side_length}{self.unit}, area: {area}{self.unit}")

class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        area = self.calculate_area()
        print(f"Длина прямоугольника: {self.__length}{self.unit}, width: {self.__width}{self.unit}, area: {area}{self.unit}")

if __name__ == "__main__":
    shapes = [
        Sguare(7),
        Sguare(5),
        Rectangle(7, 8),
        Rectangle(3, 9),
        Rectangle(9, 14)
    ]

    for shape in shapes:
        shape.info()
