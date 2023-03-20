import pygame

from Player import Player

if __name__ == "__main__":
    pygame.init()

    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    bg_img = pygame.image.load('images/background.jpg')
    bg_img = pygame.transform.scale(bg_img, (width, height))

    my_font = pygame.font.Font(pygame.font.get_default_font(), 25)

    clock = pygame.time.Clock()

    player = Player(direction=1, img="images/icon.png")
    moving_direction = -1

    running = True
    while running:
        text_surface = my_font.render(f'x: {round(player.x)}, y: {round(player.y)}', False, (80, 80, 80))

        player_pos = abs(round(player.x)) % width
        player_pos *= (1 if round(player.x) < 0 else -1)
        window.blit(bg_img, (-width + player_pos, 0))
        window.blit(bg_img, (0 + player_pos, 0))
        window.blit(bg_img, (width + player_pos, 0))

        player.render(window)
        window.blit(text_surface, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    moving_direction = 3
                elif event.key == pygame.K_RIGHT:
                    moving_direction = 1
                elif event.key == pygame.K_UP:
                    player.jump()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    moving_direction = -1

        dt = clock.tick(60)
        player.move(moving_direction, dt)
        pygame.display.update()

    pygame.quit()
