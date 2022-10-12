from curses.textpad import rectangle

from kivy.app import App
# Window.size = (320, 600)
from kivy.clock import Clock
from kivy.core.audio import SoundLoader, Sound
from kivy.core.window import Window
from kivy.graphics import Canvas, Line, Rectangle, Color
from kivy.properties import NumericProperty
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.widget import Widget
from FlappyBird import FlappyBird


class SplashScreen(Screen):
    progress = NumericProperty(0)

    def __init__(self, **kwargs):
        super(SplashScreen, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 2)

    def update(self, dt):
        if self.progress == 100:
            sm.current = "Introduction"
        self.progress += 10


class SettingsScreen(Screen):

    btns = []
    btn_texts = ['Back','Sound','Level','Locations' ]
    def __init__(self, **kwargs):
        super(SettingsScreen,self).__init__(**kwargs)
        self.init_btns()

    def init_background(self):
        with self.canvas.before:
            Color(rgb=(0,0,1,.8))
            Rectangle(size=(self.width,self.height))

    def on_enter(self, *args):
        self.btns[0].bind(on_press=self.back_)
        self.init_background()
        Clock.schedule_interval(self.update_, 1 / 60)

    def back_(self,obj):
        sm.current = "Introduction"

    def init_btns(self):
        for i in range(0,4):
            bt = Button(size_hint=(.3,.1))
            self.add_widget(bt)
            self.btns.append(bt)

    def update_btn_pos(self):
        index = 0
        text_index = 0
        for i in self.btns:
            i.pos_hint = {"center_x": .5, "center_y":.15 + index}
            i.text = self.btn_texts[text_index]
            index += .15
            text_index += 1

    def on_size(self,v,o):
        self.init_background()
    def update_(self,dt):
        self.update_btn_pos()

class AboutScreen(Screen):
    pass

class IntroScreen(Screen):
    x = 0
    X = None
    background = None
    container = None
    button = []
    alert = None
    popup = None
    btn_texts = ['Exit', 'About', 'Settings', 'High Scores', 'Play']

    def __init__(self, **kwargs):
        super(IntroScreen, self).__init__(**kwargs)
        x, y = Window.size
        with self.canvas.before:
            self.X = Color(rgb=(.1, .1, 0, 1))
            self.background = Rectangle(size=(x, y))
        self.init_btns()

    def init_container(self):
        with self.canvas:
            Color(rgb=(1, 1, 1, 1))
            self.container = Line(rounded_rectangle=(self.width * .3, self.height * .3, 200, 200, 50))

    def on_enter(self, *args):
        Clock.schedule_interval(self.updat, 1)
        self.button[0].bind(on_press=self.exit)
        self.button[1].bind(on_press=self.about)
        self.button[2].bind(on_press=self.settings)
        self.button[3].bind(on_press=self.highscore)
        self.button[4].bind(on_press=self.play)

    def highscore(self,obj):
        sm.current="High Score"

    def play(self,obj):
        sm.current = "Play"

    def about(self,obj):
        sm.current = "About"

    def settings(self,obj):
        sm.current = "Settings"

    def exit(self,obj):
        self.popup = FloatLayout()
        self.add_widget(self.popup)
        with self.popup.canvas.before:
            Color(rgb=(.1,.1,.1,.1))
            Rectangle(size=(self.width,self.height))
        text = Label(text="Are you sure ?")
        btn_yes = Button(text="Yes",pos_hint={"center_x":.62,"center_y": .4},size_hint=(.2,.1))
        btn_yes.bind(on_press=self.on_press_yes)
        btn_no = Button(text="No",pos_hint={"center_x":.32,"center_y": .4},size_hint=(.2,.1))
        btn_no.bind(on_press=self.on_press_no)
        self.popup.add_widget(btn_yes)
        self.popup.add_widget(btn_no)
        self.popup.add_widget(text)

    def on_press_yes(self,obj):
        exit(0)

    def on_press_no(self,obj):
        self.remove_widget(self.popup)

    def init_btns(self):
        layout = Widget()
        self.add_widget(layout)
        for i in range(0, 5):
            btn = Button(size=(0, 0))
            layout.add_widget(btn)
            self.button.append(btn)

    def update_btn_positions(self):
        space_factor = 0
        index = 0
        for i in self.button:
            i.size = (200, 60)
            i.pos = (self.width * .5 - 100, self.height * .2 - 30 + space_factor)
            i.text = self.btn_texts[index]
            index += 1
            space_factor += 70


    def on_size(self, *args):
        self.background.size = (self.width, self.height)

    def updat(self, dt):
        self.update_btn_positions()

        if self.x < 1:
            self.x += 0.1
            self.X.b += 0.01
        else:
            self.x = 0
            self.X.b = 0
            self.X.r = 0.2


class Play(Screen):
    def __init__(self, **kw):
        super().__init__(**kw)

    def on_enter(self, *args):
        x = FlappyBird()
        self.add_widget(x)



class Main(App):

    def build(self):
        global sm
        sm = ScreenManager()
        sm.add_widget(SplashScreen(name="Splash"))
        sm.add_widget(IntroScreen(name="Introduction"))
        sm.add_widget(Play(name="Play"))
        sm.add_widget(SettingsScreen(name="Settings"))
        sm.add_widget(AboutScreen(name="About"))

        sm.current = "Introduction"
        return sm


if __name__ == "__main__":
    Main().run()
