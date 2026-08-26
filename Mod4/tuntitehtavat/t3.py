print("This story will put you into the tale. You'll have to choose for the sake of your life!")
user_name = input("Tell us your name, traveller: ")

print("\nChoose your weapon: ")
print("1. A rubber duck that squeaks agressively")
print("2. A stale baguette (surprisingly sharp)")
print("Don't try anything else!")

weapon_choise = input("Enter 1 or 2: ").strip()

weapon = ["rubber duck", "stale baguette", "a surprisingly heavy Spoon"]


if weapon_choise == "1":
    user_weapon = weapon[0]
    battle_sound = "*SQUEAK SQUEAK*"
    effect = "instantly deafening all enemies with high-pitched doom."
elif weapon_choise == "2":
    user_weapon = weapon[1]
    battle_sound = "*CRUNCH*"
    effect = "shattering the dark lord's shield like cheap glass."
else:
    user_weapon = weapon[2]
    battle_sound = "*CLINK*"
    effect = "leaving everyone mildly confused."


story = f"""
--- THE LEGEND OF {user_name.upper()} ---

The ancient dragon roared, unleashing a wave of fury across the battlefield. 
The mighty warrior {user_name} stepped forward, holding high their legendary arms: {user_weapon}!

The dragon paused, looking utterly bewildered. 

With a battle cry, {user_name} charged forward. {battle_sound}! 
The power of {user_weapon} was unmatched, {effect}

The dragon threw its hands up in surrender, bought {user_name} a coffee, 
and they both lived weirdly ever after.
"""

print(story)