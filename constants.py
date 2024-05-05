import pygame

#window properties
WIDTH = 800
HEIGHT = 600

TITLE = "Tower Of Hanoi AI"
ICON = pygame.image.load("game-logo.png")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GOLD = (239, 229, 51)
BLUE = (78,162,196)
GREY = (170, 170, 170)
GREEN = (77, 206, 145)
LGREEN = (141,217,199)
Lblue = (60,218,245)

# Define stations dimensions
ST_WIDTH = 200
ST_HEIGHT = 25
ST_SPACING = 50
ST_PADDING = 50
ST_OFFSET = 50

# Define font
pygame.font.init()
font = pygame.font.SysFont(None, 21)

# Rods
ROD_WIDTH = 10
ROD_HEIGHT = 300
ROD_COLOR = GREY
ROD_Y = HEIGHT - ROD_HEIGHT - (50 + ST_HEIGHT)

#indecator
IND_WIDTH = 10
IND_HEIGHT = IND_WIDTH
IND_COLOR = RED
IND_OFFSET = 30

# Number of disks
NUM_DISKS = 3
DISK_WIDTH = 30
DISK_HEIGHT = 20
DISK_COLOR = BLUE
DISK_SPACING = 5

disks = [[(WIDTH // 4 - DISK_WIDTH // 2, HEIGHT - (i + 1) * DISK_HEIGHT),
          (WIDTH // 4 + DISK_WIDTH // 2, HEIGHT - i * DISK_HEIGHT)] for i in range(NUM_DISKS)]

