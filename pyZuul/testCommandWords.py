##
# Written By Zackery Salzwedel
# This file tests the functions of the CommandWords collection
# See project NOTES.txt for more information.
##
from CommandWords import CommandWords


commands = CommandWords()
print(commands.get_string_words())
print(commands.get_command_word("go"))
print(commands.get_command_word("quit"))
print(commands.get_command_word("help"))
print(commands.get_command_word("unknown"))
print(commands.get_command_word("unknown:blearg"))
print(commands.get_command_word("unknown:graelb"))
