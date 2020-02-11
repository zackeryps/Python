##
# Written By Zackery Salzwedel
# This file tests the functions of the Room class
# See project NOTES.txt for more information.
##
from Room import Room

batcave = Room("The Batcave")
manor = Room("Wayne Manor")
grounds = Room("Manor Grounds")
batcave.set_exit("up", manor)
batcave.set_exit("out", grounds)
manor.set_exit("down", batcave)
manor.set_exit("out", grounds)
grounds.set_exit("in", manor)

print("\nprinting room descriptions")
print("batcave: " + batcave.get_description())
print("manor: " + manor.get_description())
print("grounds: " + grounds.get_description())

print("\nprinting verbose descriptions")
print("batcave: " + batcave.get_description_verbose())
print("manor: " + manor.get_description_verbose())
print("grounds: " + grounds.get_description_verbose())

print("\ntesting get_exit()")
print("batcave up: " + batcave.get_exit("up").get_description())
print("batcave out: " + batcave.get_exit("out").get_description())
print("manor down: " + manor.get_exit("down").get_description())
print("manor out: " + manor.get_exit("out").get_description())
print("grounds in: " + grounds.get_exit("in").get_description())
if grounds.get_exit("down") is not None:
    print("grounds down: " + grounds.get_exit("down"))
else:
    print("grounds down: None")
