import pygame as pg
import math
import constants as c
from turret_data import TURRET_DATA

class Turret(pg.sprite.Sprite):
  def __init__(self, sprite_sheets, tile_x, tile_y):
    pg.sprite.Sprite.__init__(self)
    self.upgrade_level = 1
    self.sprite_sheets = sprite_sheets
    self.angle = 0
    self.target = None
    self.last_shot = 0
    self.load_turret_data()
    self.set_position(tile_x, tile_y)
    self.selected = False
    self.load_animation()

  def load_turret_data(self):
    turret_info = TURRET_DATA[self.upgrade_level - 1]
    self.range = turret_info["range"]
    self.cooldown = turret_info["cooldown"]
    self.damage_multiplier = 1.0

  def set_position(self, tile_x, tile_y):
    self.tile_x, self.tile_y = tile_x, tile_y
    self.x = (self.tile_x + 0.5) * c.TILE_SIZE
    self.y = (self.tile_y + 0.5) * c.TILE_SIZE
    self.rect = pg.Rect(0, 0, 0, 0)

  def load_animation(self):
    self.animation_list = self.load_images(self.sprite_sheets[self.upgrade_level - 1])
    self.frame_index = 0
    self.update_time = pg.time.get_ticks()
    self.original_image = self.animation_list[self.frame_index]
    self.image = pg.transform.rotate(self.original_image, self.angle)
    self.set_range_image()

  def load_images(self, sprite_sheet):
    size = sprite_sheet.get_height()
    return [sprite_sheet.subsurface(x * size, 0, size, size) for x in range(c.ANIMATION_STEPS)]

  def set_range_image(self):
    self.range_image = pg.Surface((self.range * 2, self.range * 2))
    self.range_image.fill((0, 0, 0))
    self.range_image.set_colorkey((0, 0, 0))
    pg.draw.circle(self.range_image, "grey100", (self.range, self.range), self.range)
    self.range_image.set_alpha(100)
    self.range_rect = self.range_image.get_rect()
    self.range_rect.center = self.rect.center

  def update(self, enemy_group, world):
    if self.target:
        self.play_animation()
    else:
        if pg.time.get_ticks() - self.last_shot > (self.cooldown / world.game_speed):
            self.pick_target(enemy_group)

  def pick_target(self, enemy_group):
    for enemy in enemy_group:
      if enemy.health > 0 and self.is_enemy_in_range(enemy):
        self.target = enemy
        self.angle = math.degrees(math.atan2(-enemy.pos[1] + self.y, enemy.pos[0] - self.x))
        self.damage_enemy()
        break

  def is_enemy_in_range(self, enemy):
    x_dist = enemy.pos[0] - self.x
    y_dist = enemy.pos[1] - self.y
    dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
    return dist < self.range

  def damage_enemy(self):
    self.target.health -= c.DAMAGE * self.damage_multiplier

  def play_animation(self):
    self.original_image = self.animation_list[self.frame_index]
    if pg.time.get_ticks() - self.update_time > c.ANIMATION_DELAY:
      self.update_time = pg.time.get_ticks()
      self.frame_index = (self.frame_index + 1) % len(self.animation_list)
      if self.frame_index == 0:
        self.last_shot = pg.time.get_ticks()
        self.target = None

  def upgrade(self):
    self.upgrade_level += 1
    self.load_turret_data()
    self.load_animation()

  def draw(self, surface):
    self.image = pg.transform.rotate(self.original_image, self.angle - 90)
    self.rect = self.image.get_rect(center=(self.x, self.y))
    surface.blit(self.image, self.rect)
    if self.selected:
      surface.blit(self.range_image, self.range_rect)
