##
# Written By Zackery Salzwedel
# This file tests the functions of the Parser class
# See project NOTES.txt for more information.
##
from Parser import Parser


print("\ntesting command printing")
print(Parser.string_commands())

print("\ntesting input : command conversion")
print("get help : " + Parser.parse_command("get help").get_command_word().value)
print("do thing : " + Parser.parse_command("do thing").get_command_word().value)
print("unknown : " + Parser.parse_command("unknown").get_command_word().value)
print("go north : " + Parser.parse_command("go north").get_command_word().value)
print("help : " + Parser.parse_command("help").get_command_word().value)
print("quit : " + Parser.parse_command("quit").get_command_word().value)
