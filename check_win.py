import pygame

def check_win(rods, num_discs):
    # Check if all discs are on the last rod
    return len(rods[2]) == num_discs

def display_win_message(screen, score):
    alert_font = pygame.font.Font(None, 50)
    alert_text = alert_font.render("You Win in " + str(score) + " steps!", True, (0, 0, 0))
    alert_rect = alert_text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
    screen.blit(alert_text, alert_rect)
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
                return

