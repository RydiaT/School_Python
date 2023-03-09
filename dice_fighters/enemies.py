def get_area_enemies(area):
    if area == 1:
        slime = [5, 1, 2, 2]
        rabbit = [7, 2, 2, 5]
        next_area = 15
        enemies = [slime, rabbit]
    
    return [enemies, next_area]

def battle_loop(enemy, player):
    enemy_hp = enemy[0]
    player_hp = player[0]

