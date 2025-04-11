import pygame


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
    main_loop()
    pygame.quit()