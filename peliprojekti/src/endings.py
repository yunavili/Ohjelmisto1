from src import world


def check_endings(player):
    # Ending 1: player dies
    if player.player_hp <= 0:
        print("\nENDING 1: DEATH")
        print("Westeros has claimed another traveler.")
        return True

    # Ending 2: player meets NPC and chooses to leave with them
    if player.met_npc:
        print("\nENDING 2: A NEW ALLIANCE")
        print("You leave Westeros together with Jon Snow.")
        print("Perhaps survival was never meant to be a solo adventure.")
        return True

    # Ending 3: all enemies have been defeated
    all_enemies_defeated = True

    for enemy in world.enemies:
        if enemy.player_hp > 0:
            all_enemies_defeated = False

    if all_enemies_defeated:
        print("\nENDING 3: THE SURVIVOR")
        print("You defeated every enemy standing in your way.")
        print("Against all odds, you survived Westeros.")
        return True

    return False
