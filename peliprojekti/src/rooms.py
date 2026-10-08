class Room:
    def __init__(self, name, item=None, enemy=None, characters=None, description="Nothing special here.", interactions=None):
        self.name = name
        self.item = item
        self.enemy = enemy
        self.characters = characters or []
        self.description = description
        self.interactions = interactions or {}

    def item_granting(self):
        if not self.item:
            print("There is no item here to take.")
            return None

        granting_choice = input(f"Do you want to collect {self.item.name}?\n1. Yes\n2. No\n> ").strip().capitalize()
        if granting_choice in ["1", "Yes"]:
            picked_item = self.item
            self.item = None
            return picked_item
        else:
            print("You chose not to pick up the item.")
            return None

    def inspect(self):
        print(self.description)

    def interact(self, action):
        if action in self.interactions:
            print(self.interactions[action])
        else:
            print("The silence in the room just got significantly more awkward.")

    def show_interactions(self):
        if not self.interactions:
            print("There is nothing interesting to interact with here.")
            return

        print("Available interactions:")

        for index, action in enumerate(self.interactions, start=1):
            print(f"{index}. {action}")
