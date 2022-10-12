import random
from platform import platform
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.graphics import Rectangle
from kivy.uix.widget import Widget
from Cloud import Cloud
from Color import color
from Pipes import Pipe


class FlappyBird(Widget):
    from user_action import keyboard_closed,on_keyboard_down,on_keyboard_up
    c = None
    clouds = []
    pipes = []
    land = []
    bird = None
    pipe_speed = 4
    screen_size = Window.size

    def __init__(self, **kwargs):
        super(FlappyBird, self).__init__(**kwargs)
        self.create_bird()
        with self.canvas:
            color().green()

        if self.is_desktop():
            self._keyboard = Window.request_keyboard(self.keyboard_closed, self)
            self._keyboard.bind(on_key_down=self.on_keyboard_down)
            self._keyboard.bind(on_key_up=self.on_keyboard_up)

        Clock.schedule_interval(self.update, 1 / 40)

    def is_desktop(self):
        if platform in ('linux', 'win', 'macosx'):
            return True
        return True

    def create_clouds(self):
        x = int(self.height * 0.75)
        y = int(self.height * 0.9)
        v = random.randint(x, y)
        if len(self.clouds) == 0:
            c = Cloud(c_size_x=100, size_y=100, pos_x=-100, pos_y=v)
            self.add_widget(c)
            self.clouds.append(c)
        elif len(self.clouds) > 0:
            if self.clouds[-1].get_pos_x() > self.width * 0.2:
                c = Cloud(c_size_x=100, size_y=100, pos_x=-200, pos_y=v)
                self.add_widget(c)
                self.clouds.append(c)

    def app_background(self):
        with self.canvas.before:
            color().white()
            Rectangle(size=(self.width, self.height))

    def create_pipes(self):
        x,y = self.screen_size
        spacing = y - (y * 0.3)

        # dynamic heights
        h = random.randint(0,self.height-100)
        if len(self.pipes) == 0 :
            pipe = Pipe(pos=(self.width,0) , size = (50,h))
            self.add_widget(pipe)
            self.pipes.append(pipe)
        elif len(self.pipes) > 0:
            if self.pipes[-1].get_pos_x() <  spacing:
                pipe = Pipe(pos=(self.width, 0), size=(50, h))
                self.add_widget(pipe)
                self.pipes.append(pipe)

    def create_bird(self):
        x,y = self.screen_size
        with self.canvas:
            self.bird = Rectangle(source="img/birds.png" ,size=(60,50))#Image('img/birds.png')
            print(self.screen_size)
            self.bird.pos=(10,y/2)
        #self.add_widget(self.bird)


    def move_clouds(self):
        for i in self.clouds:
            i.move_cloud_x(2)
    def on_size(self,instance,value):

        pass

    def move_bird(self):
        x, y = self.bird.pos
        self.bird.pos = (x + 5,y-5)

    def update(self, dt):
        self.app_background()
        self.move_clouds()
        self.create_clouds()
        self.create_pipes()
        self.create_land()
        self.delete__pipe()
        self.move_pipes()
        self.delete_cloud()
        #self.move_bird()
        # print(self.is_desktop())

    def delete__pipe(self):
        x,y = self.pipes[0].pos
        if x < 0:
            self.remove_widget(self.pipes[0])
            del self.pipes[0]

    def delete_cloud(self):
        x = self.clouds[0].get_pos_x()
        if x > self.width:
            self.remove_widget(self.clouds[0])
            del self.clouds[0]

    def create_land(self):
        with self.canvas:
            if len(self.land)  == 0:
                color().red(0.6)
                rec = Rectangle(pos=(0,0),size=(self.width,30))
                self.land.append(rec)

    def move_pipes(self):
        for i in self.pipes:
            i.move_x(-2) #(x-self.pipe_speed,y)