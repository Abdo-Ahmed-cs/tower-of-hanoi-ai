import sys

import pygame

def check_win(rods, num_discs):
    # Check if all discs are on the last rod
    return len(rods[2]) == num_discs

def display_win_message(screen, score):
    alert_font = pygame.font.Font(None, 50)
    alert_text = alert_font.render("You Win in " + str(score) + " steps!", True, (0, 0, 0))
    alert_rect = alert_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))

    esc_text = alert_font.render("Press Esc", True, (0, 0, 0))
    esc_rect = alert_text.get_rect(center=(screen.get_width() // 2 + 70, screen.get_height() // 2 + 100))

    screen.blit(alert_text, alert_rect)
    screen.blit(esc_text, esc_rect)
    pygame.display.flip()

def press_any_key():
    # Wait for any key press or Esc key press
    while True:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    return "main_menu"  # Return "main_menu" if Esc key is pressed
                 # Return if any other key is pressed
            elif event.type == pygame.QUIT:
                sys.exit()
