##
# Written By Zackery Salzwedel
# This file tests the functions of the Game class
# See project NOTES.txt for more information.
##
from Game import Game


game = Game("default")  # name added for clarity
print("\n\nPrinting game messages:")
print("scenario list: " + Game.msg_scenario_list())
print("welcome msg: " + Game.msg_welcome())
print("help msg: " + Game.msg_help())
print("exit msg: " + Game.msg_exit())

print("\nTesting gameplay:")
print("should start in North America: " + game.current_location())
print("\ngo with no location: " + game.process_command("go"))
print("should be in North America: " + game.short_location())
print("\ngo with bad location: " + game.process_command("go blearg"))
print("should be in North America: " + game.short_location())
print("\ngoing south: " + game.process_command("go south"))
print("should be in South America: " + game.short_location())
print("\ngoing south: " + game.process_command("go south"))
print("should be in Antarctica: " + game.short_location())
print("\ngoing northwest: " + game.process_command("go northwest"))
print("should be in South America: " + game.short_location())
print("\ngoing north: " + game.process_command("go north"))
print("should be in North America: " + game.short_location())
print("\ngoing east: " + game.process_command("go east"))
print("should be in Europe: " + game.short_location())
print("\ngoing west: " + game.process_command("go west"))
print("should be in North America: " + game.short_location())

print("\ntesting other commands: ")
print("help: " + game.process_command("help"))
print("empty command: " + game.process_command(""))
print("unknown command: " + game.process_command("blearg"))
print("game's finished should be false: " + str(game.is_finished()))
print("quit: " + game.process_command("quit"))
print("game's finished should be true: " + str(game.is_finished()))
