import sys
import pygame
from constants import *


# initializing our game display window
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption(TITLE)
pygame.display.set_icon(ICON)

screen.fill(WHITE)


class Disc:
    def __init__(self, size, color, rod, position):
        self.size = size
        self.color = color
        self.rod = rod
        self.position = position

    def draw(self):
        disc_rect = pygame.Rect(self.position[0], self.position[1] - DISK_HEIGHT, self.size, DISK_HEIGHT)
        pygame.draw.rect(screen, self.color, disc_rect)
class Game():
    def __init__(self, num_discs, agent = 1):
        self.num_discs = num_discs
        self.rods = [[], [], []]
        self.init_discs()
        self.agent = agent
        self.current_pos = WIDTH // 4 - ST_WIDTH // 4 - ROD_WIDTH // 2
        self.current_rod = 1
        self.selected_disc = None
        print(self.rods)
    def draw_stations(self):
        # Create rectangles
        rect1 = pygame.Rect(ST_PADDING, HEIGHT - ST_OFFSET - ST_HEIGHT, ST_WIDTH, ST_HEIGHT)
        rect2 = pygame.Rect(ST_PADDING + ST_WIDTH + ST_SPACING, HEIGHT - ST_OFFSET - ST_HEIGHT, ST_WIDTH, ST_HEIGHT)
        rect3 = pygame.Rect(ST_PADDING + 2 * (ST_WIDTH + ST_SPACING), HEIGHT - ST_OFFSET - ST_HEIGHT, ST_WIDTH, ST_HEIGHT)

        # Set up text
        text1 = font.render("Start", True, WHITE)
        text2 = font.render("", True, WHITE)
        text3 = font.render("Finish", True, WHITE)

        pygame.draw.rect(screen, GREEN, rect1)
        pygame.draw.rect(screen, GREEN, rect2)
        pygame.draw.rect(screen, GREEN, rect3)

        text1_rect = text1.get_rect(center=rect1.center)
        text2_rect = text2.get_rect(center=rect2.center)
        text3_rect = text3.get_rect(center=rect3.center)

        # Draw text
        screen.blit(text1, text1_rect)
        screen.blit(text2, text2_rect)
        screen.blit(text3, text3_rect)

    def create_indicator(self):
        indicator_top = (self.current_pos + IND_WIDTH // 2, HEIGHT - IND_OFFSET - IND_HEIGHT)
        indicator_left = (self.current_pos, HEIGHT - IND_OFFSET)
        indicator_right = (self.current_pos + IND_WIDTH, HEIGHT - IND_OFFSET)
        pygame.draw.polygon(screen, RED, [indicator_top, indicator_left, indicator_right])
    def move_indicator(self, direction):
        if direction == 'left' and self.current_rod > 1:
            self.current_rod -= 1
            self.current_pos -= (ST_WIDTH + ST_SPACING)
            # Update the indicator position
            self.create_indicator()

        elif direction == 'right' and self.current_rod < 3:
            self.current_rod += 1
            self.current_pos += (ST_WIDTH + ST_SPACING)
            # Update the indicator position
            self.create_indicator()

        self.redraw_scene()
    def draw_rods(self):
        rod1_x = WIDTH // 4 - ROD_WIDTH // 2 - (ST_WIDTH / 4)
        rod2_x = WIDTH // 2 - ROD_WIDTH // 2
        rod3_x = 3 * WIDTH // 4 - ROD_WIDTH // 2 + (ST_WIDTH / 4)

        # Create rod rectangles
        rod1 = pygame.Rect(rod1_x, ROD_Y, ROD_WIDTH, ROD_HEIGHT)
        rod2 = pygame.Rect(rod2_x, ROD_Y, ROD_WIDTH, ROD_HEIGHT)
        rod3 = pygame.Rect(rod3_x, ROD_Y, ROD_WIDTH, ROD_HEIGHT)

        # Draw rods
        pygame.draw.rect(screen, ROD_COLOR, rod1)
        pygame.draw.rect(screen, ROD_COLOR, rod2)
        pygame.draw.rect(screen, ROD_COLOR, rod3)

    def init_discs(self):
        for i in range(self.num_discs, 0, -1):
            size = i * (DISK_WIDTH // self.num_discs)
            color = (20, 20, 255 - i * (200 // self.num_discs))
            position_x = WIDTH // 4 - ST_WIDTH // 4 - size // 2
            position_y = HEIGHT - (self.num_discs - i + 1) * (DISK_HEIGHT + DISK_SPACING) - ST_OFFSET - (ST_HEIGHT / 2)
            disc = Disc(size, color, 1, (position_x, position_y))
            self.rods[0].append(disc)

    def move_top_disc(self, direction):

        current_rod = self.rods[self.current_rod - 1]

        if direction == 'up' and len(current_rod) != 0 and self.selected_disc is None:
            # Move the disc up
            self.selected_disc = current_rod[-1]
            print(self.selected_disc.size)
            self.selected_disc.position = (
                self.selected_disc.position[0],
                200
            )

        elif direction == 'down' and self.selected_disc is not None:
            if len(current_rod) != 0 and self.selected_disc.size > current_rod[-1].size:
                return
            # Move the disc down

            self.rods[self.selected_disc.rod - 1].remove(self.selected_disc)

            self.selected_disc.position = (
                self.selected_disc.position[0],
                500 - len(current_rod) * (DISK_HEIGHT) - DISK_SPACING * (len(current_rod) - 2)
            )

            self.selected_disc.rod = self.current_rod
            current_rod.append(self.selected_disc)
            self.selected_disc = None

            print([len(self.rods[0]), len(self.rods[1]), len(self.rods[2])])
        elif self.selected_disc is not None:
            if direction == 'left':
                new_position_x = self.selected_disc.position[0] - (ST_WIDTH + ST_SPACING)
                if new_position_x >= 0:
                    self.selected_disc.position = (new_position_x, self.selected_disc.position[1])
            elif direction == 'right':
                new_position_x = self.selected_disc.position[0] + (ST_WIDTH + ST_SPACING)
                if new_position_x + self.selected_disc.size <= WIDTH:
                    self.selected_disc.position = (new_position_x, self.selected_disc.position[1])
        self.redraw_scene()
    def draw_discs(self):
        for rod in self.rods:
            for disc in rod:
                disc.draw()

    def calculate_position(self, rod):
        if rod == 0:
            return WIDTH // 4 - ST_WIDTH // 4 - (self.rods[rod][-1].size // 2 if self.rods[rod] else 0)
        elif rod == 1:
            return WIDTH // 2 - (self.rods[rod][-1].size // 2 if self.rods[rod] else 0)
        else:
            return 3 * WIDTH // 4 - ROD_WIDTH // 2 + ST_WIDTH // 4 - (
                self.rods[rod][-1].size // 2 if self.rods[rod] else 0)
    def main_loop(self):
        clock = pygame.time.Clock()
        running = True

        while running:
            clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.move_indicator('left')
                        self.move_top_disc('left')
                    elif event.key == pygame.K_RIGHT:
                        self.move_indicator('right')
                        self.move_top_disc('right')
                    elif event.key == pygame.K_UP:
                        self.move_top_disc('up')
                    elif event.key == pygame.K_DOWN:
                        self.move_top_disc('down')

            self.redraw_scene()

        pygame.quit()
        sys.exit()

    def redraw_scene(self):
        screen.fill(WHITE)
        self.draw_stations()
        self.create_indicator()
        self.draw_rods()
        self.draw_discs()
        pygame.display.flip()

if __name__ == "__main__":
    game = Game(3)
    game.main_loop()