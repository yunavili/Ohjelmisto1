"""Westerosi Traveler - game entry point."""

from src import world
from src.game import run_game, setup_player
from src.intro import write_intro_files


def main():
    write_intro_files()

    player = setup_player(world.player)

    run_game(player)


if __name__ == "__main__":
    main()
