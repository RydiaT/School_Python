from player import setup_player
from enemies import get_area_enemies


print("Hello brave adventurer, welcome to our land of hilariusly unfair RNG.")
print("Let us hope you are either lucky enough to survive, or rich enough to not care.")
print("To begin with, let us create your character.")

player = setup_player()
avaliable_enemies = get_area_enemies(1)

print(f"{player[0]}, it is time to begin your adventure. Don't die.")

print(f'It is time for your first battle against a... slime. If you lose this, you\'re not allowed back home.')

currentEnemy = avaliable_enemies[0][0]

