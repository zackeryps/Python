##
# Written By Zackery Salzwedel
# This file tests the functions of the Command class
# See project NOTES.txt for more information.
##
from CommandWord import CommandWord
from Command import Command


print("making commands: cmd,_ ; do,thing ; GO,north ; QUIT,_ ; HELP,_ ")
command0 = Command("cmd")
command1 = Command("do", "thing")
command2 = Command(CommandWord.GO.value, "north")
command3 = Command(CommandWord.QUIT)
command4 = Command(CommandWord.HELP)

print("\ntesting has_second_word()")
print(command0.has_second_word())
print(command1.has_second_word())
print(command2.has_second_word())
print(command3.has_second_word())
print(command4.has_second_word())

print("\ntesting is_unknown()")
print(command0.is_unknown())
print(command1.is_unknown())
print(command2.is_unknown())
print(command3.is_unknown())
print(command4.is_unknown())

print("\ntesting get_command_word()")
print(command0.get_command_word())
print(command1.get_command_word())
print(command2.get_command_word())
print(command3.get_command_word())
print(command4.get_command_word())

print("\ntesting get_second_word()")
print(command0.get_second_word())
print(command1.get_second_word())
print(command2.get_second_word())
print(command3.get_second_word())
print(command4.get_second_word())
