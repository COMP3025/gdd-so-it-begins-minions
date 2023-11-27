def generate_enemy_spawn_data(num_levels, max_enemy_count, growth_rate):
    spawn_data = []

    for level in range(1, num_levels + 1):
        level_data = {
            "weak": level,
            "medium": level,
            "strong": level,
            "elite": level
        }
        spawn_data.append(level_data)

    return spawn_data

def generate_enemy_data(base_health, health_multiplier, base_speed, speed_multiplier, num_levels):
    enemy_data = {}

    for enemy_type in ["weak", "medium", "strong", "elite"]:
        enemy_stats = {
            "health": base_health[enemy_type] + health_multiplier[enemy_type] * num_levels,
            "speed": base_speed[enemy_type] + speed_multiplier[enemy_type] * num_levels
        }
        enemy_data[enemy_type] = enemy_stats

    return enemy_data

num_levels = 15
max_enemy_count = 100

growth_rate = 5

base_health = {"weak": 10, "medium": 15, "strong": 20, "elite": 30}
health_multiplier = {"weak": 5, "medium": 10, "strong": 15, "elite": 20}

base_speed = {"weak": 2, "medium": 3, "strong": 4, "elite": 6}
speed_multiplier = {"weak": 1, "medium": 2, "strong": 3, "elite": 4}

ENEMY_SPAWN_DATA = generate_enemy_spawn_data(num_levels, max_enemy_count, growth_rate)
ENEMY_DATA = generate_enemy_data(base_health, health_multiplier, base_speed, speed_multiplier, num_levels)
