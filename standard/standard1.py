class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def diameter(self):
        return 2 * self._radius


circle = Circle(5)
print(circle.diameter)
