import pygame
import random


class Food(pygame.sprite.Sprite):
    def __init__(self, group, size):
        super().__init__(group)
        self.size = (size, size)
        self.surf = pygame.Surface(self.size)
        self.surf.fill("red")
        self.rect = self.surf.get_rect()

    def draw(self, screen: pygame.Surface):
        screen.blit(self.surf, self.rect)

    def random_pos(self, area_size):
        x = random.randrange(0, area_size[0])
        y = random.randrange(0, area_size[1])
        self.place_food(x, y)

    def place_food(self, x, y):
        self.rect.x = x * self.size[0]
        self.rect.y = y * self.size[1]
