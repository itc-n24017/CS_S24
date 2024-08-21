class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def perimeter(self):
        # 周の長さ = 2 * (幅 + 高さ)
        return 2 * (self.width + self.height)

    def area(self):
        # 面積 = 幅 * 高さ
        return self.width * self.height

class Square(Rectangle):
    def __init__(self, side_length):
        # 正方形では幅と高さが同じなので、両方にside_lengthを渡します
        super().__init__(side_length, side_length)

# 例として、幅4、高さ6の長方形を作成して、周の長さと面積を計算します
rectangle = Rectangle(4, 6)
print("長方形の周の長さ:", rectangle.perimeter())
print("長方形の面積:", rectangle.area())

# 例として、幅4の正方形を作成して、周の長さと面積を計算します
square = Square(4)
print("正方形の周の長さ:", square.perimeter())
print("正方形の面積:", square.area())

