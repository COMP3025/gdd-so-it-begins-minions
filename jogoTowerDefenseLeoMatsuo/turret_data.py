import random

def generate_turret_data(base_range, range_increment, base_cooldown, cooldown_decrement, num_levels):
    turret_data = []

    for level in range(1, num_levels + 1):
        turret_info = {
            "range": base_range + (level - 1) * range_increment,
            "cooldown": max(base_cooldown - (level - 1) * cooldown_decrement, 100)
        }
        turret_data.append(turret_info)

    return turret_data

base_range = 90
range_increment = 20
base_cooldown = 1500
cooldown_decrement = 150
num_levels = 4

TURRET_DATA = generate_turret_data(base_range, range_increment, base_cooldown, cooldown_decrement, num_levels)
