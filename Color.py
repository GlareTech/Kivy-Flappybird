from kivy.graphics import Color


class color:
    def __init__(self, **kwargs):
        # print(kwargs)
        pass

    def red(self, opacity=1):
        # with self.canvas:
        Color(rgb=(1, 0, 0, opacity))

    def green(self, opacity=1):
        Color(rgb=(0, 1, 0, opacity))

    def white(self,opacity=1):
        Color(rgb=(1,1,1,opacity))

    def black(self,opacity = 1):
        Color(rgb=(0,0,0,opacity))

    def blue(self,opacity = 1):
        Color(rgb = (0,0,1,opacity))