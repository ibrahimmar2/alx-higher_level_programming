from models.base import Base
"""Module for Rectangle class"""


class Rectangle(Base):
    '''
        Defining the Rectangle class
        Inherits from:
            Base
    '''
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, data):
        if not isinstance(data, int):
            raise TypeError("width must be an integer")
        if data < 0:
            raise ValueError(" width must be > 0")
        self.__width = data

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, data):
        if not isinstance(data, int):
            raise TypeError(" height must be an integer")
        if data < 0:
            raise ValueError(" height must be > 0")
        self.__height = data

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, data):
        if not isinstance(data, int):
            raise TypeError(" x must be an integer")
        if data < 0:
            raise ValueError("x must be > 0")
        self.__x = data

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, data):
        if not isinstance(data, int):
            raise TypeError(" y must be an integer")
        if data < 0:
            raise ValueError(" y must be >= 0")
        self.__y = data

    def area(self):

        return (self.__height * self.__width)

    def display(self):
        print("\n"*self.y, end="")
        for x in range(self.height):
            print(" " * self.x, end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        return (
            "[Rectangle] ({}) {}/{} - {}/{}"
            .format(self.id, self.__x, self.__y, self.__width, self.__height)
            )

    def update(self, *args, **kwargs):
        properties = ['id', 'width', 'height', 'x', 'y']
        if args:
            for i, arg in enumerate(args):
                if i < len(properties):
                    setattr(self, properties[i], arg)
        else:
            for key, value in kwargs.items():
                if key in properties:
                    setattr(self, key, value)
