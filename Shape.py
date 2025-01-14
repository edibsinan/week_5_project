class Shape:
    def __init__(self, width, height):
        self.width=width
        self.height=height

class Rectangle(Shape):
    def calculate_area(self):
        return self.width*self.height
    
class Square(Shape):
    def calculate_area(self):
        if self.width!=self.height:
            raise ValueError("width and heigth must be equal for a square")
        return self.width*self.height


# Rectangle örneği oluşturma
rect=Rectangle(5,10)
print(f"rectangle area: {rect.calculate_area()}")

# Square örneği oluşturma
square=Square(5,5)
print(f"square area: {square.calculate_area()}")