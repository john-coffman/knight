import pygame


class Weapon():
    def __init__(self, pos):
        self.rect = pygame.Rect(1280/2, 680/2, pos[0], pos[1])
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 4
        self.gravity = .08

    def weapon_movement(self):
        if pygame.MOUSEMOTION:
            self.rect.y += pygame.mouse.get_rel()[1]

        if self.rect.bottom >= 720:
            self.direction.y += -self.gravity
            self.rect.y += self.direction.y
        else:
            self.apply_gravity()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def update(self):
        self.weapon_movement()
