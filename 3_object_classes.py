class Circle(object):
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color
    def add_radius(self, r):
        self.radius = self.radius + r
        return(self.radius)
circle_1 = Circle(5, "blue")
print(circle_1.radius)
circle_1.radius = 10
print(circle_1.radius)
circle_1.add_radius(2)
print(circle_1.radius)