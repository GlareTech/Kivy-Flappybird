from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.graphics.context_instructions import Image
from kivy.uix.widget import Widget

from Color import color


class Pipe(Widget):
    width = 50
    height = 0
    x = 0
    y = 0
    pos = ()
    size= ()
    screen_max_x = None
    screen_max_y = None
    pipe_body = None
    pipe_top = None
    pipe_body_from_top = None
    pipe_top_from_top = None

    def __init__(self, **kwargs):
        super(Pipe, self).__init__(**kwargs)
        self.create_pipe()
        #self.pos = (0, 0)
    def on_size(self,instance):
        print("hi")
    def create_pipe(self):
        #print(Window.size)
        self.width, self.height = self.size
        #print(self.size)
        with self.canvas:
            color().green()
            self.pipe_body = Rectangle(size=(self.width, self.height), pos=self.pos)
            u, v = self.pos
            self.pipe_top = Rectangle(size=(self.width + 20, 30), pos=(u - 10, v + self.height))

            w,h= Window.size

            # 25% space btw top and bottom pipes
            xr = h * 0.25
            pipe_height = h - xr - (self.height + 30)
            self.pipe_body_from_top = Rectangle(size=(self.width,pipe_height),pos=(u,v + self.height+xr+30))
            self.pipe_top_from_top = Rectangle(size=(self.width + 20, 30), pos=(u - 10, v + self.height+xr))

    def move_x(self,value):
        # reset Positions
        x,y = self.pipe_top.pos
        x1,y1 = self.pipe_body.pos

        x2,y2 = self.pipe_body_from_top.pos
        x3,y3 = self.pipe_top_from_top.pos

        self.pipe_top_from_top.pos = (x3+value,y3)
        self.pipe_body_from_top.pos = (x2+value,y2)
        self.pipe_body.pos = (x1+value,y1)
        self.pipe_top.pos = (x+value,y)

        u,v = self.pos
        self.pos = (u+value,v)

    def get_pos_x(self):
        x,y =self.pos
        return x