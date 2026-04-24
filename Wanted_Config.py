import pygame
import Wanted_Config
import sys
import Wanted_Main_Loop
import os


def restart_program(self):  # restarts the program
    Wanted_Main_Loop.main()
    sys.exit()

class ScreenManager:
    def __init__(self, screen):
        self.screen = screen
        self.font = Wanted_Config.font
        self.bg_color = (0, 0, 0)

    def draw_text_top_left(self, text, color, x=100, y=100):
        surf = self.font.render(text, True, color)
        self.screen.blit(surf, (x, y))

    def draw_centered_text(self, text, color, y_offset=0):
        surf = self.font.render(text, True, color)
        rect = surf.get_rect(center=(Wanted_Config.res[0] // 2, Wanted_Config.res[1] // 2 + y_offset))
        self.screen.blit(surf, rect)

    def wait_for_click_or_key(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                    waiting = False

            pygame.display.flip()
            pygame.time.Clock().tick(Wanted_Config.fps)

    def wait_for_end(self):
        waiting = True
        while waiting:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        restart_program(self)
                        waiting = False
                if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN] and event.type != pygame.K_r:
                    pygame.quit()
                    exit()

            pygame.display.flip()
            pygame.time.Clock().tick(Wanted_Config.fps)

    def show_start_screen(self):
        self.screen.fill(self.bg_color)
        self.draw_centered_text("WANTED!", Wanted_Config.white, -60)
        self.draw_centered_text("Click to Start, Esc to Exit Anytime", Wanted_Config.green, 20)
        pygame.display.flip()
        self.draw_centered_text("Credits to Shutterstock and Pixabay for assets", Wanted_Config.green, 200)
        pygame.display.flip()
        self.wait_for_click_or_key()

    def show_next_round_screen(self, round_num):
        self.screen.fill(self.bg_color)
        self.draw_centered_text(f"Round {round_num}", Wanted_Config.white, -60)
        self.draw_centered_text("Get Ready!", Wanted_Config.green, 20)
        pygame.display.flip()
        self.wait_for_click_or_key() #Click through to see the different Round screens

    def show_game_over_screen(self, score):
        self.screen.fill(self.bg_color)
        self.draw_centered_text("GAME OVER", Wanted_Config.red, -60)
        self.draw_centered_text(f"Score: {score}", Wanted_Config.white, 0)
        self.draw_centered_text("Press R to restart game.", Wanted_Config.green, 60)
        self.draw_centered_text("Press anything else to exit.", Wanted_Config.green, 100)
        pygame.display.flip()
        self.wait_for_end()



