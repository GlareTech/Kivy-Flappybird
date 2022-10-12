from kivy.graphics import Canvas, Rectangle, Ellipse, Color
from kivy.properties import NumericProperty, ObjectProperty
from kivy.uix.widget import Widget

from Color import color


class Cloud(Widget):
    c_size_x = NumericProperty(0)
    size_y = NumericProperty(0)
    pos_x = NumericProperty(0)
    pos_y = NumericProperty(0)

    rectangle = None
    Ellipse_Start = None
    Ellipse_End = None
    Ellipse_Top = ObjectProperty()

    def __init__(self, **kwargs):
        super(Cloud, self).__init__(**kwargs)
        # print(str(**kwargs))

        #print(self.pos_y)
        self.create()

    def create(self):
        def pos_x(self, value):
            self.pos_x = value

        def pos_y(self, value):
            self.pos_y = value

        with self.canvas:
            color().black()
            self.rectangle = Rectangle(pos=(self.pos_x, self.pos_y), size=(self.c_size_x, self.size_y))
            c_pos_x = self.pos_x - self.c_size_x / 2
            c_pos_y = self.pos_y
            self.Ellipse_Start = Ellipse(pos=(c_pos_x, c_pos_y), size=(self.c_size_x, self.size_y))
            # Color(rgb=(.8, .8, 1, .2))
            c_pos_x2 = self.pos_x + self.c_size_x / 2
            c_pos_y2 = self.pos_y
            self.Ellipse_End = Ellipse(pos=(c_pos_x2, c_pos_y2), size=(self.c_size_x, self.size_y))

            c_pos_x3 = self.pos_x - self.c_size_x / 5
            c_pos_y3 = self.pos_y + self.size_y / 4

            self.Ellipse_Top = Ellipse(pos=(c_pos_x3, c_pos_y3), size=(self.c_size_x + 10, self.size_y + 10))

    def move_cloud_x(self, increment):
        # previous values
        x, y = self.rectangle.pos
        x1, y1 = self.Ellipse_Start.pos
        x2, y2 = self.Ellipse_End.pos
        x3, y3 = self.Ellipse_Top.pos

        self.rectangle.pos = (x + increment, y)
        self.Ellipse_Start.pos = (x1 + increment, y1)
        self.Ellipse_End.pos = (x2 + increment, y2)
        self.Ellipse_Top.pos = (x3 + increment, y3)
        self.pos_x += increment

    def set_pos_x(self, value):
        self.pos_x = value

    def set_pos_y(self, value):
        self.pos_y = value

    def set_size_x(self, value):
        self.c_size_x = value

    def set_size_y(self, value):
        self.size_y = value

    def set_position(self,x,y):
        self.pos_x,self.pos_y = x,y

    def get_size(self):
        x, y = self.rectangle.size
        x1, y1 = self.Ellipse_Start.size
        x2, y2 = self.Ellipse_End.size
        x3, y3 = self.Ellipse_Top.size


        return (x+(x1/2)+(x2/2),y+y3/4)

    def get_position(self):
        return (self.pos_x,self.pos_y)

    def get_pos_x(self):
        return self.pos_x

    def get_pos_y(self):
        return self.pos_y