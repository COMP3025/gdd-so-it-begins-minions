import pygame as pg
import json
from enemy import Enemy
from world import World
from turret import Turret
from button import Button
import constants as c

pg.init()

clock = pg.time.Clock()

screen = pg.display.set_mode((c.SCREEN_WIDTH + c.SIDE_PANEL, c.SCREEN_HEIGHT))
pg.display.set_caption("Tower Defence")

placing_turrets = False

map_image = pg.image.load('levels/level.png').convert_alpha()
turret_sheet = pg.image.load('assets/images/turrets/turret_1.png').convert_alpha()
cursor_turret = pg.image.load('assets/images/turrets/cursor_turret.png').convert_alpha()
enemy_image = pg.image.load('assets/images/enemies/enemy_1.png').convert_alpha()
buy_turret_image = pg.image.load('assets/images/buttons/buy_turret.png').convert_alpha()
cancel_image = pg.image.load('assets/images/buttons/cancel.png').convert_alpha()

with open('levels/level.tmj') as file:
  world_data = json.load(file)

def create_turret(mouse_pos):
  mouse_tile_x = mouse_pos[0] // c.TILE_SIZE
  mouse_tile_y = mouse_pos[1] // c.TILE_SIZE
  mouse_tile_num = (mouse_tile_y * c.COLS) + mouse_tile_x
  if world.tile_map[mouse_tile_num] == 7:
    space_is_free = True
    for turret in turret_group:
      if (mouse_tile_x, mouse_tile_y) == (turret.tile_x, turret.tile_y):
        space_is_free = False
    if space_is_free == True:
      new_turret = Turret(turret_sheet, mouse_tile_x, mouse_tile_y)
      turret_group.add(new_turret)

world = World(world_data, map_image)
world.process_data()

enemy_group = pg.sprite.Group()
turret_group = pg.sprite.Group()

enemy = Enemy(world.waypoints, enemy_image)
enemy_group.add(enemy)

turret_button = Button(c.SCREEN_WIDTH + 30, 120, buy_turret_image, True)
cancel_button = Button(c.SCREEN_WIDTH + 50, 180, cancel_image, True)

run = True
while run:

  clock.tick(c.FPS)

  enemy_group.update()
  turret_group.update()

  screen.fill("grey100")

  world.draw(screen)

  enemy_group.draw(screen)
  turret_group.draw(screen)

  if turret_button.draw(screen):
    placing_turrets = True
  if placing_turrets == True:
    cursor_rect = cursor_turret.get_rect()
    cursor_pos = pg.mouse.get_pos()
    cursor_rect.center = cursor_pos
    if cursor_pos[0] <= c.SCREEN_WIDTH:
      screen.blit(cursor_turret, cursor_rect)
    if cancel_button.draw(screen):
      placing_turrets = False

  for event in pg.event.get():
    if event.type == pg.QUIT:
      run = False
    if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
      mouse_pos = pg.mouse.get_pos()
      if mouse_pos[0] < c.SCREEN_WIDTH and mouse_pos[1] < c.SCREEN_HEIGHT:
        if placing_turrets == True:
          create_turret(mouse_pos)
          
  pg.display.flip()

pg.quit()