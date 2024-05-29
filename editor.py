from settings import *
from map_data import *
from objects import *
from hud import *

class Editor():
    def __init__(self):
        #Initialize map data:
        self.map = tile_map
        self.tile_data = tile_data
        self.tilemap = Tilemap(self.map, self.tile_data, 0, 0)

        self.current_tile = 2

        self.camera = Camera()

        #Input properties:
        self.current_key = "NULL"
        self.current_mouse = "NULL"
        self.key_timer = 0
        self.key_timer_max = 10
        self.mouse_timer = 0
        self.mouse_timer_max = 1

        self.hud = Hud()

    def update(self, window, keys, delta_time):
        self.hud.current_tile_forward.check_if_pressed(delta_time)
        self.hud.current_tile_backward.check_if_pressed(delta_time)

        if self.current_tile < 0:
            self.current_tile = 0
        if self.current_tile > len(self.tile_data) - 3:
            self.current_tile = len(self.tile_data) - 3
            
        self.handle_keyboard_input(keys, delta_time)
        if self.current_key == "RIGHT":
            self.add_width()

        if self.current_key == "DOWN":
            self.add_height()

        if self.current_key == "LEFT":
            self.subtract_width()

        if self.current_key == "UP":
            self.subtract_height()

        if self.current_key == "2" and self.current_tile < len(self.tile_data ) - 3:
            self.current_tile += 1
        
        if self.current_key == "1" and self.current_tile > 0:
            self.current_tile -= 1

        if self.hud.current_tile_forward.is_pressed and self.current_tile < len(self.tile_data ) - 3:
            self.current_tile += 1

        if self.hud.current_tile_backward.is_pressed and self.current_tile > 0:
            self.current_tile -= 1

        if pygame.mouse.get_pressed()[0]:
            self.draw_tile()

        self.update_hud(delta_time)
        self.render(window)

    def render(self, window):
        self.walls, self.platforms, self.decor = self.tilemap.render()
        self.tiles = self.camera.render(self.walls + self.platforms + self.decor)

        for tile in self.tiles:
            window.blit(tile[2], (tile[0], tile[1]))

        self.hud.render(window, self.tile_data, self.current_tile)

    def update_hud(self, delta_time):
        if self.current_key == "SPACE":
            if self.hud.state == "OPEN":
                self.hud.state = "CLOSED"

            elif self.hud.state == "CLOSED":
                self.hud.state = "OPEN"
        
        self.hud.update(delta_time)

    def handle_mouse_input(self, delta_time):
        pass
    
    def handle_keyboard_input(self, keys, delta_time):
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

        if keys[pygame.K_2] and self.key_timer <= 0:
            self.current_key = "2"
            self.key_timer = self.key_timer_max * delta_time

        if keys[pygame.K_1] and self.key_timer <= 0:
            self.current_key = "1"
            self.key_timer = self.key_timer_max * delta_time

        if keys[pygame.K_SPACE] and self.key_timer <= 0:
            self.current_key = "SPACE"
            self.key_timer = self.key_timer_max * delta_time

        if self.key_timer > 0:
            self.key_timer -= 1 * delta_time

        if self.key_timer < self.key_timer_max * delta_time - 1 * delta_time:
            self.current_key = "NULL"

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
        return (pygame.mouse.get_pos()[0]//16 + 1, pygame.mouse.get_pos()[1]//16 + 1)
    
    def draw_tile(self):
        if self.get_pos()[0] <= self.get_width() and self.get_pos()[1] <= self.get_height():
            self.map[self.get_pos()[1] - 1][self.get_pos()[0] - 1] = self.current_tile
