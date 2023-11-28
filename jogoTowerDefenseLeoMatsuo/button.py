import pygame as pg

class Button:
  def __init__(self, x, y, image, is_single_click):
    self.image = image
    self.rect = self.image.get_rect()
    self.rect.topleft = (x, y)
    self.is_clicked = False
    self.is_single_click = is_single_click

  def draw(self, surface):
    has_action = False
    mouse_position = pg.mouse.get_pos()

    if self.rect.collidepoint(mouse_position):
        if pg.mouse.get_pressed()[0] == 1 and not self.is_clicked:
            has_action = True
            if self.is_single_click:
                self.is_clicked = True

    if pg.mouse.get_pressed()[0] == 0:
        self.is_clicked = False

    surface.blit(self.image, self.rect)

    return has_action