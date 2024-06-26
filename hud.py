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
        self.state = "OPEN"
        self.open_y = window_height - 64
        self.closed_y = window_height - 16

        #Initialize menu elements:
        self.cur_tile_x = 0
        self.cur_tile_y = 0

        self.width = Text()
        self.height = Text()

        #Initialize buttons:
        self.cur_tile_forward = Button(sprites["RIGHTARROW"])
        self.cur_tile_backward = Button(sprites["LEFTARROW"])

        self.add_width = Button(sprites["RIGHTARROW"])
        self.subtract_width = Button(sprites["LEFTARROW"])

        self.add_height = Button(sprites["RIGHTARROW"])
        self.subtract_height = Button(sprites["LEFTARROW"])

        self.menu_trans = Button(sprites["NULL"])
        self.menu_trans.width, self.menu_trans.height = 16, 16#Give bigger hitbox.

        self.cam_up = Button(sprites["UPARROW"])
        self.cam_down = Button(sprites["DOWNARROW"])
        self.cam_right = Button(sprites["RIGHTARROW"])
        self.cam_left = Button(sprites["LEFTARROW"])
        
    def update(self, delta_time, width, height):
        self.update_buttons(delta_time)
        self.update_text(width, height)
        self.update_tile_display()

        if self.state == "OPEN":
            self.handle_open_state(delta_time)

        if self.state == "CLOSED":
            self.handle_closed_state(delta_time)

    def render(self, window, tile_data, current_tile):
        window.blit(self.hud_bg, (self.x, self.y))#Draw hud background.

        #Draw hud elements:
        window.blit(tile_data[current_tile], (self.cur_tile_x, self.cur_tile_y))
        self.width.render(window)
        self.height.render(window)

        #Draw buttons:
        window.blit(self.cur_tile_forward.sprite, (self.cur_tile_forward.x, self.cur_tile_forward.y))
        window.blit(self.cur_tile_backward.sprite, (self.cur_tile_backward.x, self.cur_tile_backward.y))

        window.blit(self.add_width.sprite, (self.add_width.x, self.add_width.y))
        window.blit(self.subtract_width.sprite, (self.subtract_width.x, self.subtract_width.y))

        window.blit(self.add_height.sprite, (self.add_height.x, self.add_height.y))
        window.blit(self.subtract_height.sprite, (self.subtract_height.x, self.subtract_height.y))

        window.blit(sprites["CAMERA"], (self.x + 152, self.y + 32))
        window.blit(self.cam_up.sprite, (self.cam_up.x, self.cam_up.y))
        window.blit(self.cam_down.sprite, (self.cam_down.x, self.cam_down.y))
        window.blit(self.cam_right.sprite, (self.cam_right.x, self.cam_right.y))
        window.blit(self.cam_left.sprite, (self.cam_left.x, self.cam_left.y))

        window.blit(self.menu_trans.sprite, (self.menu_trans.x, self.menu_trans.y))

    def update_buttons(self, delta_time):
        #Anchor button positions on hud:
        self.cur_tile_backward.x = self.x + 8
        self.cur_tile_backward.y = self.y + 36

        self.cur_tile_forward.x = self.x + 48
        self.cur_tile_forward.y = self.y + 36

        self.add_width.x = self.x + 120
        self.add_width.y = self.y + 32

        self.subtract_width.x = self.x + 72
        self.subtract_width.y = self.y + 32

        self.add_height.x = self.x + 120
        self.add_height.y = self.y + 40

        self.subtract_height.x = self.x + 72
        self.subtract_height.y = self.y + 40

        self.menu_trans.x = self.x + 120
        self.menu_trans.y = self.y

        self.cam_up.x = self.x + 156
        self.cam_up.y = self.y + 24

        self.cam_down.x = self.x + 156
        self.cam_down.y = self.y + 48

        self.cam_right.x = self.x + 170
        self.cam_right.y = self.y + 36

        self.cam_left.x = self.x + 143
        self.cam_left.y = self.y + 36

        #Check for button presses.
        self.cur_tile_backward.check_if_pressed(delta_time)
        self.cur_tile_forward.check_if_pressed(delta_time)
        self.add_width.check_if_pressed(delta_time)
        self.subtract_width.check_if_pressed(delta_time)
        self.add_height.check_if_pressed(delta_time)
        self.subtract_height.check_if_pressed(delta_time)
        self.menu_trans.check_if_pressed(delta_time)
        self.cam_up.check_if_pressed(delta_time)
        self.cam_down.check_if_pressed(delta_time)
        self.cam_right.check_if_pressed(delta_time)
        self.cam_left.check_if_pressed(delta_time)

    def update_text(self, width, height):
        self.width.text = "W:"+str(width)
        self.height.text = "H:"+str(height)
        self.width.x = self.x + 80
        self.width.y = self.y + 32

        self.height.x = self.x + 80
        self.height.y = self.y + 40

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
        
    