import pygame as pg
import random
import constants as c
from enemy_data import ENEMY_SPAWN_DATA

class World:
  def __init__(self, data, map_image):
    self.level = 1
    self.game_speed = 1
    self.health = c.HEALTH
    self.money = c.MONEY
    self.tile_map = []
    self.waypoints = []
    self.level_data = data
    self.image = map_image
    self.enemy_list = []
    self.spawned_enemies = 0
    self.killed_enemies = 0
    self.missed_enemies = 0

  def process_data(self):
    for layer in self.level_data["layers"]:
        if layer["name"] == "tilemap":
            self.tile_map = layer["data"]
        elif layer["name"] == "waypoints":
            self.process_waypoints(layer["objects"][0]["polyline"])

  def process_waypoints(self, data):
    self.waypoints.extend((point["x"], point["y"]) for point in data)

  def process_enemies(self):
    enemies = ENEMY_SPAWN_DATA[self.level - 1]
    self.enemy_list = [enemy_type for enemy_type, count in enemies.items() for _ in range(count)]
    random.shuffle(self.enemy_list)

  def check_level_complete(self):
    return (self.killed_enemies + self.missed_enemies) == len(self.enemy_list)

  def reset_level(self):
      self.enemy_list = []
      self.spawned_enemies = self.killed_enemies = self.missed_enemies = 0

  def draw(self, surface):
      surface.blit(self.image, (0, 0))