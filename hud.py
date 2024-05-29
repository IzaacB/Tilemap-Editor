from settings import *
class Hud():
    def __init__(self):
        self.status_bar = pygame.image.load("Sprites/StatusBar.png")
        self.x, self.y = 0, window_height
        self.speed = 300

        self.state = "OPEN"
        self.open_y = window_height - 32
        self.closed_y = window_height
        
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

    def render(self, window):
        window.blit(self.status_bar, (self.x, self.y))