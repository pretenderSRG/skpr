from math import pi


class Circle:

    def __init__(self, radius):
        if type(radius) not in (int, float):
            raise TypeError("Радіус повинен бути числом")
        if radius < 0:
            raise ValueError("Радіус повине бути невід'ємним")
        self.radius = radius

    def get_radius(self):
        return self.radius

    def get_diameter(self):
        return self.radius * 2

    def get_perimeter(self):
        return round(pi * self.radius ** 2, 2)

