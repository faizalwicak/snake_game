import pygame
from .sprites.food import Food
from .sprites.head import Head
from .sprites.tail import Tail


EVENT_MOVE = pygame.USEREVENT + 1


class Gameplay:
    def __init__(self, move_speed, area_size, block_size, screen) -> None:
        self.move_speed = move_speed
        self.area_size = area_size
        self.block_size = block_size
        self.screen = screen
        self.score = 0

    def run(self):
        clock = pygame.time.Clock()

        pygame.time.set_timer(EVENT_MOVE, self.move_speed)

        largeFont = pygame.font.SysFont("comicsans", 12)  # creates a font object
    
        head = Head(self.block_size)
        head.update_loc((3, 0))

        tails = pygame.sprite.Group()
        for i in range(3):
            t = Tail(tails, self.block_size)
            t.update_loc((2 - i, 0))

        foods = pygame.sprite.Group()
        food = Food(foods, self.block_size)
        food.random_pos(self.area_size)
        while pygame.sprite.spritecollide(
            head, foods, False
        ) or pygame.sprite.groupcollide(tails, foods, False, False):
            food.random_pos(self.area_size)

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

                if event.type == EVENT_MOVE:
                    last_block = head.rect.copy()
                    head.update()
                    for i in tails:
                        l = i.rect.copy()
                        i.rect = last_block
                        last_block = l

                    if pygame.sprite.spritecollide(head, foods, False):
                        while pygame.sprite.spritecollide(
                            head, foods, False
                        ) or pygame.sprite.groupcollide(tails, foods, False, False):
                            food.random_pos(self.area_size)

                        tail = Tail(tails, self.block_size)
                        tail.rect = last_block
                        self.score += 1

                    if pygame.sprite.spritecollideany(head, tails):
                        running = False

                    if (
                        head.rect.x < 0
                        or head.rect.y < 0
                        or head.rect.x >= self.area_size[0] * self.block_size
                        or head.rect.y >= self.area_size[1] * self.block_size
                    ):
                        running = False

            self.screen.fill("white")

            pressed_keys = pygame.key.get_pressed()

            for i in tails:
                i.draw(self.screen)

            head.draw(self.screen)
            head.update_dir(pressed_keys)

            for i in tails:
                i.draw(self.screen)

            for i in foods:
                i.draw(self.screen)

            score_text = largeFont.render("Your Score: " + str(self.score), 1, (0, 0, 255))
            self.screen.blit(score_text, (0, 0))

            pygame.display.flip()

            clock.tick(60)

        return self.score
