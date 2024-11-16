import pygame
from gamesprites import Player
WIDTH = 1200
HEIGHT = 600
FPS = 60


class Game:
    def __init__(self, backgraound_filename=None):
        self.window = pygame.display.set_mode((WIDTH,HEIGHT))
        self.clock = pygame.time.Clock()

        if backgraound_filename is not None:
            self.background = pygame.transform.scale(
                                pygame.image.load(backgraound_filename),
                                (WIDTH,HEIGHT)
                                )
            
    def create_player(self, coords,size):
        self.player = Player ("player.png", coords, size)
    
    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            self.player.draw(self.window)
            self.player.update()

            
            pygame.display.flip()
            self.clock.tick(FPS)

if __name__ == "__main__":
    game = Game()
    game.run()