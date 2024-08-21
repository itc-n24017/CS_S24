import math

class Cylinder:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def surface_area(self):
        # 表面積 = 2πrh + 2πr^2
        base_area = 2 * math.pi * self.radius ** 2
        side_area = 2 * math.pi * self.radius * self.height
        return base_area + side_area

    def volume(self):
        # 体積 = πr^2h
        return math.pi * self.radius ** 2 * self.height

# 例として、半径3、高さ5の円柱を作成して、表面積と体積を計算します
cylinder = Cylinder(3, 5)
print("表面積:", cylinder.surface_area())
print("体積:", cylinder.volume())

