def keyboard_closed(self):
    self.keyboard.unbind(on_key_down=self.on_keyboard_down)
    self.keyboard.unbind(on_key_up=self.on_keyboard_up)
    self.keyboard = None

def on_touch_up(self, touch):
    print("up")



def on_touch_down(self, touch):
    if touch.x < self.width / 2:
        print('<-')

    else:
        print("->")



def on_keyboard_down(self, keyboard, keycode, text, modifiers):
    x, y = self.bird.pos
    if keycode[1] == 'up':
        self.bird.pos = (x, y+5)
    elif keycode[1] == 'down':
        self.bird.pos = (x, y-5)
    elif keycode[1] == 'right':
        self.bird.pos = (x+5, y)
    elif keycode[1] == 'left':
        self.bird.pos = (x-5,y)
    return True


def on_keyboard_up(self, keyboard, keycode):
    x,y = self.bird.pos
    # self.bird.pos = (x+2,y-5)
    return True
