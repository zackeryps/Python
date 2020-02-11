##
# Written By Zackery Salzwedel
# This class simply activates the game class of zuul.
# Room building and Command logic is in the game class.
# See project NOTES.txt for more information.
##
from Game import Game


def main():
    print(Game.msg_scenario_list())
    game = Game(input("Please pick a scenario: ").lower())
    print(Game.msg_welcome())
    while not game.is_finished():
        print(game.current_location())
        print(game.process_command(input("Enter a command: ").lower()))
    print(game.msg_exit())


main()

##
# Original Java does not have a driver file or a main.
# This is because it was made for use with BlueJ.
## v2
# Moved game logic flow control to driver.
##
