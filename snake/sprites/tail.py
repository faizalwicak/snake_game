import pygame


class Tail(pygame.sprite.Sprite):
    def __init__(self, group, size):
        super().__init__(group)

        self.size = size
        self.surf = pygame.Surface((size, size))
        self.surf.fill("black")
        self.rect = self.surf.get_rect()

    def draw(self, screen):
        screen.blit(self.surf, self.rect)

    def update_loc(self, loc):
        self.rect.x = self.size * loc[0]
        self.rect.y = self.size * loc[1]
