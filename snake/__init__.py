import pygame
import pygame_menu

from snake.gameplay import Gameplay
from snake.score import Score


class Snake:
    def __init__(self, area_size=(10, 10), block_size=50):
        self.area_size = area_size
        self.block_size = block_size

        self.size = (
            self.area_size[0] * self.block_size,
            self.area_size[1] * self.block_size,
        )

        self.move_speed = 300

        pygame.init()
        self.screen = pygame.display.set_mode(self.size)

    def menu(self):
        def set_difficulty(value, difficulty):
            self.move_speed = difficulty
            pass

        def start_the_game():
            self.run()

        menu = pygame_menu.Menu(
            "Snake by zalwi017",
            self.size[0],
            self.size[1],
            theme=pygame_menu.themes.THEME_BLUE,
        )

        menu.add.selector(
            "Difficulty :",
            [("Hard", 200), ("Normal", 300), ("Easy", 400)],
            default=1,
            onchange=set_difficulty,
        )
        menu.add.button("Play", start_the_game)
        menu.add.button("Quit", pygame_menu.events.EXIT)

        menu.mainloop(self.screen)

    def run(self):
        gameplay = Gameplay(self.move_speed, self.area_size, self.block_size, self.screen)
        score = gameplay.run()
        score_screen = Score(self.screen, self.size, score)
        score_screen.run()
