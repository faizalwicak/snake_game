import pygame


MOVE_UP = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_RIGHT = 3


class Head:
    def __init__(self, size):
        super().__init__()
        self.dir = MOVE_RIGHT
        self.dir_now = self.dir

        self.size = size
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill("black")
        self.rect = self.surf.get_rect()

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update_loc(self, loc):
        self.rect.x = self.size * loc[0]
        self.rect.y = self.size * loc[1]

    def update(self):
        if self.dir == MOVE_RIGHT:
            self.rect.move_ip(self.size, 0)
        elif self.dir == MOVE_LEFT:
            self.rect.move_ip(-self.size, 0)
        elif self.dir == MOVE_UP:
            self.rect.move_ip(0, -self.size)
        elif self.dir == MOVE_DOWN:
            self.rect.move_ip(0, self.size)

        self.dir_now = self.dir

    def update_dir(self, pressed_keys):
        if pressed_keys[pygame.K_UP] and self.dir_now != MOVE_DOWN:
            self.dir = MOVE_UP
        if pressed_keys[pygame.K_DOWN] and self.dir_now != MOVE_UP:
            self.dir = MOVE_DOWN
        if pressed_keys[pygame.K_LEFT] and self.dir_now != MOVE_RIGHT:
            self.dir = MOVE_LEFT
        if pressed_keys[pygame.K_RIGHT] and self.dir_now != MOVE_LEFT:
            self.dir = MOVE_RIGHT
