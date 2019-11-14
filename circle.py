"""
The circle should have a radius, a diameter, and an area. 
It should also have a nice string representation.

For example:

>>> c = Circle(5)
>>> c
Circle(5)
>>> c.radius
5
>>> c.diameter
10
>>> c.area
78.53981633974483
Additionally the radius should default to 1 if no radius is specified when you create your circle:

>>> c = Circle()
>>> c.radius
1
>>> c.diameter
2

Other:
The first bonus required that when we change the radius, the diameter and area change automatically.
The second bonus required that the diameter property be able to be set to a value and that the radius would automatically change appropriately based on the set value.
For this bonus, we're supposed to make it so that the radius attribute cannot be set to a negative number.
"""


import math


class Circle:

    """Circle with radius, area, and diameter."""

    def __init__(self, radius=1):
        self.radius = radius
        if radius < 0:
            raise ValueError("Radius cannot be negative")

    def __repr__(self):
        return f'Circle({self.radius})'

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def diameter(self):
        return self.radius * 2

    @diameter.setter
    def diameter(self, diameter):
        self.radius = diameter / 2




