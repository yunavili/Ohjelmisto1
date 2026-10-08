def fight(player, enemy):
    print(f"\nA fight begins against {enemy.name}!")

    while player.player_hp > 0 and enemy.player_hp > 0:

        print(f"\nYour HP: {player.player_hp}/{player.max_hp}")
        print(f"{enemy.name} HP: {enemy.player_hp}/{enemy.max_hp}")

        print("\n1. Attack")
        print("2. Run")

        choice = input("> ").strip()

        if choice == "1":

            player.attack(enemy)

            if enemy.player_hp <= 0:
                print(f"\nYou defeated the {enemy.name}!")

                # If enemy has loot, put it into the room.
                if enemy.loot is not None:
                    enemy.place.item = enemy.loot
                    print(f"{enemy.name} dropped {enemy.loot.name}!")

                enemy.place.enemy = None

                return True

            enemy.attack(player)

            if player.player_hp <= 0:
                print("\nYour body has officially given up on you. Game Over!")
                return False

        elif choice == "2":
            print("You escaped from the fight!")
            return False

        else:
            print("Invalid choice, please try again.")

    return False
