from settings import *
from objects import *
from sprite import *

class Hud():
    def __init__(self):
        #Initialize menu UI:
        self.x = 0
        self.y = 0
        self.hud_bg = sprites["HUDBG"]
        self.trans_speed = 300

        #Initialize menu state and associated properties:
        self.state = "CLOSED"
        self.open_y = window_height - 64
        self.closed_y = window_height - 16

        #Initialize menu elements:
        self.cur_tile_x = 0
        self.cur_tile_y = 0

        #Initialize buttons:
        self.cur_tile_forward = Button(sprites["RIGHTARROW"])

        self.cur_tile_backward = Button(sprites["LEFTARROW"])

        self.menu_trans = Button(sprites["NULL"])
        self.menu_trans.width, self.menu_trans.height = 16, 16#Give bigger hitbox.
        
    def update(self, delta_time):
        self.update_buttons(delta_time)
        self.update_tile_display()

        if self.state == "OPEN":
            self.handle_open_state(delta_time)

        if self.state == "CLOSED":
            self.handle_closed_state(delta_time)

    def render(self, window, tile_data, current_tile):
        window.blit(self.hud_bg, (self.x, self.y))#Draw hud background.

        #Draw hud elements:
        window.blit(tile_data[current_tile], (self.cur_tile_x, self.cur_tile_y))

        #Draw buttons:
        window.blit(self.cur_tile_forward.sprite, (self.cur_tile_forward.x, self.cur_tile_forward.y))

        window.blit(self.cur_tile_backward.sprite, (self.cur_tile_backward.x, self.cur_tile_backward.y))

        window.blit(self.menu_trans.sprite, (self.menu_trans.x, self.menu_trans.y))

    def update_buttons(self, delta_time):
        #Anchor button positions on hud:
        self.cur_tile_backward.x = self.x + 16
        self.cur_tile_backward.y = self.y + 48

        self.cur_tile_forward.x = self.x + 32
        self.cur_tile_forward.y = self.y + 48

        self.menu_trans.x = self.x + 120
        self.menu_trans.y = self.y

        #Check for button presses.
        self.cur_tile_backward.check_if_pressed(delta_time)
        self.cur_tile_forward.check_if_pressed(delta_time)
        self.menu_trans.check_if_pressed(delta_time)

    def update_tile_display(self):
        #Anchor tile display to hud:
        self.cur_tile_x = self.x + 24
        self.cur_tile_y = self.y + 31

    def handle_open_state(self, delta_time):
        #Transition if not in position:
        if self.y > self.open_y:
            self.y -= self.trans_speed * delta_time

        if self.y <= self.open_y + self.trans_speed * delta_time:
            self.y = self.open_y

    def handle_closed_state(self, delta_time):
        #Transition if not in position:
        if self.y < self.closed_y:
            self.y += self.trans_speed * delta_time

        if self.y >= self.closed_y - self.trans_speed * delta_time:
            self.y = self.closed_y
        
    