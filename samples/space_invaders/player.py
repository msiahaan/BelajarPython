import pygame


class Player(object):
	def __init__(self):
		self.img = pygame.image.load("player.png")
		self.x = 370
		self.y = 480
		self.x_change = 0
		self.y_change = 0
		self.lives = 3
          
def draw_player(img, x, y):
	screen.blit(img, (x, y))

def main_loop():
   
    running = True
    while running:

        # RGB: Red, Green, Blue
        screen.fill((0, 0, 0))
        screen.blit(background, (0, 0))  
        # pool of events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # RENDER YOUR GAME HERE
        # draw the player
        draw_player(player.img, player.x, player.y)
        # update the display
        pygame.display.update()

        clock.tick(60)  # limits FPS to 60

if __name__ == "__main__":
    # pygame setup
    pygame.init()

    icon = pygame.image.load("ufo.png")
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Space Invaders")
    
    # Background
    background = pygame.image.load("background.png")
    clock = pygame.time.Clock()
    # add player
    player = Player()
    # main loop
    main_loop()
    pygame.quit()