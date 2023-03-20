"""

Класс, описывающий игрока

Игрок имеет координаты x, y и вектор направления зрения

"""
import pygame


class Player:
    directions = ((0, -1), (1, 0), (0, 1), (-1, 0))
    player_width, player_height = 150, 200
    player_y_pos = 340
    player_speed = 700
    player_jump_speed = 400
    player_jump = 200

    def __init__(self, x=0, y=0, direction=0, img=None):
        self.x = x
        self.y = Player.player_y_pos
        self.direction = direction
        self.image = img
        self.in_jump = -1

    def change_direction(self, new_direction: int):
        self.direction = new_direction

    def move(self, move_direction: int, dt):
        if move_direction != -1:
            self.change_direction(move_direction)
            delta = (dt / 10000) * Player.player_speed
            self.x += Player.directions[self.direction][0] * delta
            self.y += Player.directions[self.direction][1] * delta

        delta = (dt / 1000) * Player.player_jump_speed
        if self.in_jump == 0:
            if self.y > Player.player_y_pos - Player.player_jump:
                self.y -= delta
            if self.y <= Player.player_y_pos - Player.player_jump:
                self.y = Player.player_y_pos - Player.player_jump
                self.in_jump = 1
        else:
            if self.y < Player.player_y_pos:
                self.y += delta
            if self.y >= Player.player_y_pos:
                self.y = Player.player_y_pos
                self.in_jump = -1

    def jump(self):
        if self.in_jump == -1: # start jump
            self.in_jump = 0

    def render(self, window):
        assert self.image is not None

        images_path = self.image.split('.')
        image_path = images_path[0] + "_" + str(self.direction) + "." + images_path[1]
        img = pygame.image.load(image_path).convert_alpha()
        img = pygame.transform.scale(img, (Player.player_width, Player.player_height))
        window.blit(img, (800 // 2 - 150 // 2, self.y))



