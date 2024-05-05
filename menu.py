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

    # Initialize agent variable
    agent = 1

    # Main menu loop
    running = True
    while running:
        screen.fill(LGREEN)

        # Display main menu options
        title_text = font1.render("Tower of Hanoi", True, GOLD)
        title_text_shadow = font1.render("Tower of Hanoi", True, BLACK)
        title_rect = title_text.get_rect(center=(WIDTH // 2, 100))

        discs_text = font2.render(f"{num_discs}", True, BLACK)
        discs_rect = discs_text.get_rect(center=(WIDTH // 2, 240))  # Reduced space around the number of discs

        difficulty_text = font3.render("Difficulty Level", True, BLACK)
        difficulty_rect = difficulty_text.get_rect(center=(WIDTH // 2, 180))

        agent_text = font3.render("Agent", True, BLACK)
        agent_rect = agent_text.get_rect(center=(WIDTH // 2, 315))

        player_text = font2.render("Player", True, BLACK)
        player_rect = player_text.get_rect(center=(WIDTH // 2.6, 380))

        ai_text = font2.render("AI", True, BLACK)
        ai_rect = ai_text.get_rect(center=(WIDTH // 1.6, 380))


        exit_text = font2.render("Exit", True, BLACK)
        exit_rect = exit_text.get_rect(center=(WIDTH // 2, 500))

        # Change the color of text based on the agent selection
        if agent == 1:
            player_text = font2.render("Player", True, WHITE)
        elif agent == 2:
            ai_text = font2.render("AI", True, WHITE)

        screen.blit(title_text_shadow, (title_rect.x + 4, title_rect.y + 4))
        screen.blit(title_text, title_rect)
        screen.blit(difficulty_text, difficulty_rect)
        screen.blit(agent_text, agent_rect)
        screen.blit(player_text, player_rect)
        screen.blit(ai_text, ai_rect)


        # Left arrow button
        left_arrow = pygame.Rect(205, 210, 50, 50)
        pygame.draw.polygon(screen, BLACK, [(220, 235), (240, 210), (240, 260)])
        if left_arrow.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.polygon(screen, WHITE, [(220, 235), (240, 210), (240, 260)], 3)

        # Right arrow button
        right_arrow = pygame.Rect(550, 210, 50, 50)
        pygame.draw.polygon(screen, BLACK, [(565, 235), (545, 210), (545, 260)])
        if right_arrow.collidepoint(pygame.mouse.get_pos()):
            pygame.draw.polygon(screen, WHITE, [(565, 235), (545, 210), (545, 260)], 3)

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
                    game = Game(num_discs, agent)
                    game.main_loop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if left_arrow.collidepoint(event.pos):
                    num_discs = max(num_discs - 1, min_discs)
                elif right_arrow.collidepoint(event.pos):
                    num_discs = min(num_discs + 1, max_discs)
                elif exit_rect.collidepoint(event.pos):  # Check if Exit button is clicked
                    running = False  # Set running to False to exit the loop
                if player_rect.collidepoint(event.pos):
                    agent = 1
                    screen.blit(player_text, player_rect)
                elif ai_rect.collidepoint(event.pos):
                    agent = 2
                    screen.blit(ai_text, ai_rect)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()