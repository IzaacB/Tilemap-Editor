from settings import *
from map_data import *
from objects import *
from hud import *

class Editor():
    def __init__(self):
        #Initialize map/tile data:
        self.map = tile_map
        self.tile_data = tile_data
        self.current_tile = 2

        #Keyboard input properties:
        self.current_key = "NULL"
        self.key_timer = 0
        self.key_timer_max = 10

        #Mouse input properties:
        self.current_mouse = "NULL"
        self.mouse_timer = 0
        self.mouse_timer_max = 5

        #Initialize visual elements:
        self.hud = Hud()
        self.camera = Camera()
        self.tilemap = Tilemap(self.map, self.tile_data, 0, 0)

    def update(self, window, keys, delta_time):        
        self.handle_raw_input(keys, delta_time)
        self.keybinds()
        self.ui_input()
        self.update_hud(delta_time)
        self.render(window)

    def render(self, window):
        self.walls, self.platforms, self.decor = self.tilemap.render()
        self.tiles = self.camera.render(self.walls + self.platforms + self.decor)

        for tile in self.tiles:
            window.blit(tile[2], (tile[0], tile[1]))

        self.hud.render(window, self.tile_data, self.current_tile)

    def update_hud(self, delta_time):
        if self.hud.menu_trans.is_pressed:
            if self.hud.state == "OPEN":
                self.hud.state = "CLOSED"

            elif self.hud.state == "CLOSED":
                self.hud.state = "OPEN"
        
        self.hud.update(delta_time, self.get_width(), self.get_height())
    
    def handle_raw_input(self, keys, delta_time):
        #Get current key pressed and put it on timer:
        if keys[pygame.K_RIGHT] and self.key_timer <= 0:
            self.current_key = "RIGHT"
            self.key_timer = self.key_timer_max * delta_time

        if keys[pygame.K_DOWN] and self.key_timer <= 0:
            self.current_key = "DOWN"
            self.key_timer = self.key_timer_max * delta_time

        if keys[pygame.K_LEFT] and self.key_timer <= 0:
            self.current_key = "LEFT"
            self.key_timer = self.key_timer_max * delta_time

        if keys[pygame.K_UP] and self.key_timer <= 0:
            self.current_key = "UP"
            self.key_timer = self.key_timer_max * delta_time

        #Get current mouse button pressed:
        if pygame.mouse.get_pressed()[0] and self.mouse_timer <= 0:
            self.current_mouse = "LEFT"
            self.mouse_timer = self.mouse_timer_max * delta_time

        #Run down timer:
        if self.key_timer > 0:
            self.key_timer -= 1 * delta_time

        if self.key_timer < self.key_timer_max * delta_time - 1 * delta_time:
            self.current_key = "NULL"

        if self.mouse_timer >0:
            self.mouse_timer -= 1 * delta_time
            
        if self.mouse_timer < self.mouse_timer_max * delta_time - 1 * delta_time:
            self.current_mouse = "NULL"

    def keybinds(self):
        #Add width/height:
        if self.current_key == "RIGHT":
            self.add_width()
        elif self.current_key == "LEFT":
            self.subtract_width()

        if self.current_key == "DOWN":
            self.add_height()
        elif self.current_key == "UP":
            self.subtract_height()

    def ui_input(self):
        if self.current_mouse == "LEFT":
            if self.hud.state == "OPEN":
                if pygame.mouse.get_pos()[1] < self.hud.y + 16 and not self.hud.menu_trans.is_hovering:
                    self.draw_tile()
            else:
                if not self.hud.menu_trans.is_hovering:
                    self.draw_tile()
        if self.hud.add_width.is_pressed:
            self.add_width()
        elif self.hud.subtract_width.is_pressed:
            self.subtract_width()

        if self.hud.cur_tile_forward.is_pressed:
            self.current_tile += 1
        elif self.hud.cur_tile_backward.is_pressed:
            self.current_tile -= 1

        if self.hud.add_height.is_pressed:
            self.add_height()
        elif self.hud.subtract_height.is_pressed:
            self.subtract_height()
                    
    def get_width(self):
        return len(self.map[0])
    
    def get_height(self):
        return len(self.map)

    def add_width(self):
        for y in range(0, len(self.map)):
            self.map[y].append(0)

    def subtract_width(self):
        if self.get_width() > 1:
            for y in range(0, len(self.map)):
                self.map[y].pop(-1)

    def add_height(self):
        self.map.append([0])
        for x in range(0, self.get_width() - 1):
            self.map[-1].append(0)

    def subtract_height(self):
        if self.get_height() > 1:
            self.map.pop(-1)

    def get_pos(self):
        return ((pygame.mouse.get_pos()[0]//16 + 1) - self.camera.x, (pygame.mouse.get_pos()[1]//16 + 1) - self.camera.y)
    
    def draw_tile(self):
        if self.get_pos()[0] <= self.get_width() and self.get_pos()[1] <= self.get_height():
            self.map[self.get_pos()[1] - 1][self.get_pos()[0] - 1] = self.current_tile
