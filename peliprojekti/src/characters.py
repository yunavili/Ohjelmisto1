class Character:
    def __init__(self, name, place, hp):
        self.name = name
        self.player_hp = hp
        self.max_hp = hp
        self.place = place

    def get_hp_status(self):
        if self.player_hp <= 0:
            return "Dead"
        elif self.player_hp < 10:
            return "Critical"
        elif self.player_hp < self.max_hp:
            return "Injured"
        else:
            return "Full Health"

    def getting_damage(self, damage):
        self.player_hp -= damage
        print(f"{self.name} took {damage} damage!")

        # Character no longer ends the whole game when HP reaches 0. Dying is not in trends these days.
        # Same works for enemies
        if self.player_hp <= 0:
            self.player_hp = 0
            return True

        return False


class Player(Character):

    def __init__(self, name, place, hp=20, max_weight=100):
        super().__init__(name, place, hp)
        self.inventory = []
        self.current_weight = 0
        self.max_weight = max_weight
        self.age = 0
        self.met_npc = False

    def move(self, room):
        self.place = room
        print(f"You have moved to the {room.name}.")

        if room.item is not None:
            print(f"{self.place.item.name.capitalize()} is shining in the room.")
        else:
            print("The room is so empty that only the wind breaks the silence.")

        if room.enemy is not None:
            print(f"{room.enemy.name} Oh no, is here!")

        if room.characters:
            for character in room.characters:
                print(f"{character.name} is in the room.")

    def collect_item(self):
        item = self.place.item_granting()
        if item:
            if self.max_weight < self.current_weight + item.weight:
                print(f"You cannot pick up {item.name}, it's too heavy! Current weight: {self.current_weight}/{self.max_weight}")
            else:
                self.current_weight += item.weight
                self.inventory.append(item)
                print(f"{item.name.capitalize()} was added. Current weight: {self.current_weight}/{self.max_weight}")
        else:
            print("There's nothing to pick up")

    def show_inventory(self):
        if not self.inventory:
            print("Your inventory is empty.")
        else:
            print("Your inventory:")
            for index, item in enumerate(self.inventory, start=1):
                print(f"{index}. {item.name.capitalize()}")

    def throw_item(self, index):
        if 0 <= index < len(self.inventory):
            item = self.inventory[index]
            self.inventory.remove(item)
            self.current_weight -= item.weight
            print(f"You threw away {item.name}. Now it's destroyed. Forever. \nCurrent weight: {self.current_weight}/{self.max_weight}")
        else:
            print("Item not in inventory")

    def healing(self, potion):
        if self.player_hp >= self.max_hp:
            print("You are already at full health!")
        else:
            self.player_hp = min(self.player_hp + potion.hp_amount, self.max_hp)
            print(f"You used a healing potion and restored {potion.hp_amount} HP! Current HP {self.player_hp}/{self.max_hp}")

    #new
    def attack(self, enemy):
        from src import world

        damage = world.dice_6.roll()

        print(f"You attack {enemy.name} and deal {damage} damage!")

        enemy.getting_damage(damage)


class Enemy(Character):
    def __init__(self, name, hp, attack, place, loot=None):
        super().__init__(name, place, hp)
        self.attack_power = attack
        self.loot = loot

    def attack(self, target_player):
        print(f"{self.name} attacks {target_player.name} for {self.attack_power} damage!")
        target_player.getting_damage(self.attack_power)


class NPC(Character):
    def __init__(self, name, place, dialigue):
        super().__init__(name, place, hp=10)
        self.dialigue = dialigue

    def talk(self):
        print(f'{self.name}: "{self.dialigue}"')
