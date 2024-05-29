from settings import *
from objects import *
from sprite import *

class Hud():
    def __init__(self):
        self.status_bar = pygame.image.load("Sprites/StatusBar.png")
        self.x, self.y = 0, window_height
        self.speed = 300

        self.state = "OPEN"
        self.open_y = window_height - 32
        self.closed_y = window_height

        self.current_tile_x, self.current_tile_y = self.x, self.y
        self.current_tile_forward = Button(sprites["RIGHTARROW"])
        self.current_tile_backward = Button(sprites["LEFTARROW"])
        
    def update(self, delta_time):
        if self.state == "OPEN":
            self.handle_open_state(delta_time)

        if self.state == "CLOSED":
            self.handle_closed_state(delta_time)

    def handle_open_state(self, delta_time):
        if self.y > self.open_y:
            self.y -= self.speed * delta_time

        if self.y <= self.open_y + self.speed * delta_time:
            self.y = self.open_y

    def handle_closed_state(self, delta_time):
        if self.y < self.closed_y:
            self.y += self.speed * delta_time

        if self.y >= self.closed_y - self.speed * delta_time:
            self.y = self.closed_y

    def display_current_tile(self, window, tile_data, current_tile):
        self.current_tile_x, self.current_tile_y = self.x + 8, self.y + 5

        self.current_tile_forward.x = self.current_tile_x + 9
        self.current_tile_forward.y = self.current_tile_y + 18

        self.current_tile_backward.x = self.current_tile_x - 1
        self.current_tile_backward.y = self.current_tile_y + 18

        window.blit(tile_data[current_tile], (self.current_tile_x, self.current_tile_y))
        window.blit(self.current_tile_forward.sprite, (self.current_tile_forward.x, self.current_tile_forward.y))
        window.blit(self.current_tile_backward.sprite, (self.current_tile_backward.x, self.current_tile_backward.y))

    def render(self, window, tile_data, current_tile):
        window.blit(self.status_bar, (self.x, self.y))
        self.display_current_tile(window, tile_data, current_tile)
