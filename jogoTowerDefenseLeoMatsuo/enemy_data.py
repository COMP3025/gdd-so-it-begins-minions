def generate_enemy_spawn_data(num_levels, max_enemy_count):
    spawn_data = []

    for level in range(1, num_levels + 1):
        level_data = {
            "weak": int(max_enemy_count * (level / num_levels)) * 10 if level <= 5 else 0,
            "medium": int(max_enemy_count * (level / num_levels)) * 10 if 2 <= level <= 10 else 0,
            "strong": int(max_enemy_count * (level / num_levels)) * 10 if 10 <= level <= 15 else 0,
            "elite":int(max_enemy_count * (level / num_levels)) * 10000 if 15 <= level <= 20 else 0, #start infinity wave
        }
        spawn_data.append(level_data)

    return spawn_data

def generate_enemy_data(base_health, health_multiplier, base_speed, speed_multiplier):
    enemy_data = {}

    for enemy_type in ["weak", "medium", "strong", "elite"]:
        enemy_stats = {
            "health": base_health[enemy_type] + health_multiplier[enemy_type],
            "speed": base_speed[enemy_type] + speed_multiplier[enemy_type]
        }
        enemy_data[enemy_type] = enemy_stats

    return enemy_data

num_levels = 20

max_enemy_count = 100

base_health = {"weak": 5, "medium": 8, "strong": 12, "elite": 16}
health_multiplier = {"weak": 1, "medium": 2, "strong": 3, "elite": 4}

base_speed = {"weak": 1.5, "medium": 2, "strong": 2, "elite": 3}
speed_multiplier = {"weak": 1, "medium": 2, "strong": 3, "elite": 4}

ENEMY_SPAWN_DATA = generate_enemy_spawn_data(num_levels, max_enemy_count)
ENEMY_DATA = generate_enemy_data(base_health, health_multiplier, base_speed, speed_multiplier)
