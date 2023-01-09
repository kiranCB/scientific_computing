class Shape_Calculator:  
    class Rectangle:
        def __init__(self, width, height):
            self.width = width
            self.height = height
            self.name = "Rectangle"

        def set_width(self, new_width):
            self.width = new_width
            return f"The width is set to {self.width}"

        def set_height(self, new_height):
            self.height = new_height
            return f"The new height is set to {self.height}"

        def get_area(self):
            return self.height * self.width

        def get_perimeter(self):
            return 2 * (self.height + self.width)

        def get_diagonal(self):
            return (self.width**2 + self.height**2) ** 0.5

        def get_picture(self):
            if self.width >= 50 or self.height >= 50:
                return "Too big for picture."
            s = f""
            print()
            for i in range(self.height):
                for j in range(self.width):
                    s += "*"
                s += "\n"
            return s

        def get_amount_inside(self,shape):
            shape_width=shape.width
            shape_length=shape.height
            return (self.width//shape_width)*(self.height//shape_length)

        def __str__(self):
            return f"{self.name}(width={self.width}, height={self.height})"


    class Square(Rectangle):
        def __init__(self, length):
            super().__init__(length, length)
            self.name = "Square"

        def set_side(self, side):
            self.width = side
            self.height = side
            return f"The side length is set to {self.width}"

        def set_width(self, new_width):
            self.width = new_width
            self.height = new_width
            return f"The width is set to {self.width}"

        def set_height(self, new_height):
            self.height = new_height
            self.width = new_height
            return f"The new height is set to {self.height}"
        def __str__(self):
            return f"{self.name}(side={self.width})"



shape_calculator=Shape_Calculator
rect = shape_calculator.Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = shape_calculator.Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))
