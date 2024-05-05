import pygame
import sys
from game import Game  # Import the Game class from your existing files
from constants import *

# Pygame initialization
pygame.init()

# Font
pygame.font.init()
font1 = pygame.font.SysFont(None, 110)
font2 = pygame.font.SysFont(None, 40)
font3 = pygame.font.SysFont(None, 45)

# Main menu function
def main_menu():
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)
    pygame.display.set_icon(ICON)

    # Counter for number of discs
    num_discs = 3
    max_discs = 6
    min_discs = 2

    # Main menu loop
    running = True
    while running:
        screen.fill(LGREEN)

        # Display main menu options
        title_text = font1.render("Tower of Hanoi", True, GOLD)
        title_text_shadow = font1.render("Tower of Hanoi", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 100))

        discs_text = font2.render(f"{num_discs}", True, BLACK)
        discs_rect = discs_text.get_rect(center=(WIDTH // 2, 360))  # Reduced space around the number of discs

        difficulty_text = font3.render("Difficulty Level", True, BLACK)
        difficulty_rect = difficulty_text.get_rect(center=(WIDTH // 2, 250))

        exit_text = font2.render("Exit", True, BLACK)
        exit_rect = exit_text.get_rect(center=(WIDTH // 2, 500))

        screen.blit(title_text_shadow, (title_rect.x + 4, title_rect.y + 4))
        screen.blit(title_text, title_rect)
        screen.blit(difficulty_text, difficulty_rect)

        # Left arrow button
        left_arrow = pygame.Rect(205, 335, 50, 50)
        pygame.draw.polygon(screen, BLACK, [(220, 360), (240, 335), (240, 385)])
        if left_arrow.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.polygon(screen, RED, [(220, 360), (240, 335), (240, 385)], 3)

        # Right arrow button
        right_arrow = pygame.Rect(550, 335, 50, 50)
        pygame.draw.polygon(screen, BLACK, [(565, 360), (545, 335), (545, 385)])
        if right_arrow.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.polygon(screen, GOLD, [(565, 360), (545, 335), (545, 385)], 3)

        screen.blit(discs_text, discs_rect)
        screen.blit(exit_text, exit_rect)

        pygame.display.flip()
        clock = pygame.time.Clock()
        clock.tick(60)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_LEFT:
                    num_discs = max(num_discs - 1, min_discs)
                elif event.key == pygame.K_RIGHT:
                    num_discs = min(num_discs + 1, max_discs)
                elif event.key == pygame.K_RETURN:
                    game = Game(num_discs)
                    game.main_loop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.collidepoint(event.pos):
                    num_discs = max(num_discs - 1, min_discs)
                elif right_arrow.collidepoint(event.pos):
                    num_discs = min(num_discs + 1, max_discs)
                elif exit_rect.collidepoint(event.pos):  # Check if Exit button is clicked
                    running = False  # Set running to False to exit the loop

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()
