##
# Written By Zackery Salzwedel
# This files tests the CommandWord enumeration
# See project NOTES.txt for more information.
##
from CommandWord import CommandWord


print("\nprinting enums directly:")
print(CommandWord.GO)
print(CommandWord.QUIT)
print(CommandWord.HELP)
print(CommandWord.UNKNOWN)

print("\nprinting enum values:")
print(CommandWord.GO.value)
print(CommandWord.QUIT.value)
print(CommandWord.HELP.value)
print(CommandWord.UNKNOWN.value)

print("\nAsserting enum values match expected:")
try:
    assert CommandWord.GO.value == "go"
    print("" + CommandWord.GO.value + " assert passed")
except AssertionError:
    print("" + CommandWord.GO.value + " assert failed")
try:
    assert CommandWord.QUIT.value == "quit"
    print("" + CommandWord.QUIT.value + " assert passed")
except AssertionError:
    print("" + CommandWord.QUIT.value + " assert failed")
try:
    assert CommandWord.HELP.value == "help"
    print("" + CommandWord.HELP.value + " assert passed")
except AssertionError:
    print("" + CommandWord.HELP.value + " assert failed")
try:
    assert CommandWord.UNKNOWN.value == "unknown"
    print("" + CommandWord.UNKNOWN.value + " assert passed")
except AssertionError:
    print("" + CommandWord.UNKNOWN.value + " assert failed")

print("\ntest complete")
