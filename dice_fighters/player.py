from random import randint


def setup_player():
    name = input("What is our hero's name? ")
    print(f"Ah, {name}, a name that will ring through the ages. Totally.")

    decision = input("Would you like to allocate your own stats or use a preset? (custom or preset) ").lower()

    if decision == 'preset':
        print('Presets: \nLucky\nGlass Cannon\nTank\nHard Mode\nStandard')
        preset = input("Which preset would you like? ").lower()

        stats = get_presets(preset)
        return [name, stats]
    elif decision == 'custom':
        stats = custom_stats_setup()
        return [name, stats]
    else:
        print("That's not an option. Goodbye.")
    

def get_presets(preset):
    # Max HP, Str, Def, Luck

    if preset == "lucky":
        return [10, 2, 2, 5]
    elif preset == "glass cannon":
        return [4, 6, 2, 3]
    elif preset == "tank":
        return [10, 2, 5, 2]
    elif preset == "hard mode":
        return [5, 1, 1, 2]
    else:
        return [3, 3, 3, 3]
    
def custom_stats_setup():
    avaliable_pts = randint(3, 15)
    stats = [1,1,1,1]

    while True:
        print(f"You currently have {avaliable_pts} points to spend\nYour stats: \nHP:{stats[0]}\nAttack:{stats[1]}\nDefense:{stats[2]}\nLuck:{stats[3]}")
        stat = input("What stat do you want to allocate too?").lower()
        pts = input("How many points?")
        pts = int(pts)
        
        while pts > avaliable_pts:
            pts = input("How many points?")
            pts = int(pts)
        
        if stat == 'hp':
            stats[0] += pts
            avaliable_pts -= pts
        elif stat == 'attack':
            stats[1] += pts
            avaliable_pts -= pts
        elif stat == 'defense':
            stats[2] += pts
            avaliable_pts -= pts
        elif stat == 'luck':
            stats[3] += pts
            avaliable_pts -= pts
        else:
            print("That's not a stat. It has to be hp, attack, defense, or luck.")
        
        if avaliable_pts == 0:
            print("You're out of points.  That's it for stat allocation!")
            break

    return stats
