import pygame
from pygame_button import Button

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ORANGE = (255, 180, 0)

BUTTON_STYLE = {
    "hover_color": BLUE,
    "clicked_color": GREEN,
    "clicked_font_color": BLACK,
    "hover_font_color": ORANGE,
}

class Score:
    def __init__(self, screen, size, score):
        self.screen = screen
        self.score = score
        self.size = size

        self.button = Button(
            (0, 0, 200, 50), (0,255,0), self.destroy, text="Menu", **BUTTON_STYLE
        )
        self.button.rect.center = (self.size[0] / 2, 100)
        self.running = True

    def destroy(self):
        self.running = False

    def run(self):
        clock = pygame.time.Clock()

        self.running = True
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                
                self.button.check_event(event)

            self.screen.fill("white")

            largeFont = pygame.font.SysFont("comicsans", 80)
            game_over = largeFont.render("Game Over", 1, (255, 0, 255))
            score = largeFont.render("Your Score: " + str(self.score), 1, (0, 0, 255))
            self.screen.blit(
                game_over, (self.size[0] / 2 - game_over.get_width() / 2, 150)
            )
            self.screen.blit(score, (self.size[0] / 2 - score.get_width() / 2, 240))


            self.button.update(self.screen)
            
            pygame.display.flip()

            clock.tick(60)
