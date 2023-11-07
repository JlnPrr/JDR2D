import pygame
from pygame import mixer
import pytmx
import pyscroll

from player import Player
from src.dialog import DialogBox
from src.map import MapManager


class Game:

    def __init__(self):
        # Démarrage
        self.running = True
        self.map = "world"

        # Affichage de la fenêtre
        self.screen = pygame.display.set_mode((1024, 728))
        pygame.display.set_caption("RPG2D")

        # MUSIC
        mixer.music.load("../sound/TownTheme.mp3")
        mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)

        # Générer le joueur
        self.player = Player()
        self.map_manager = MapManager(self.screen, self.player)
        self.dialog_box = DialogBox()

        # Définir le logo du jeu
        pygame.display.set_icon(self.player.get())

    def handle_input(self):
        pressed = pygame.key.get_pressed()

        if pressed[pygame.K_ESCAPE]:
            self.running = False
        elif pressed[pygame.K_UP]:
            self.player.move_player("up")
        elif pressed[pygame.K_DOWN]:
            self.player.move_player("down")
        elif pressed[pygame.K_RIGHT]:
            self.player.move_player("right")
        elif pressed[pygame.K_LEFT]:
            self.player.move_player("left")

    def update(self):
        self.map_manager.update()

    def run(self):

        clock = pygame.time.Clock()

        # Clock
        while self.running:

            self.player.save_location()
            self.handle_input()
            self.update()
            self.map_manager.draw()
            self.dialog_box.render(self.screen)
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.map_manager.check_npc_collisions(self.dialog_box)

            clock.tick(60)

        pygame.quit()
