##
# Written By Zackery Salzwedel
# This file tests the functions of the Scenario class
# See project NOTES.txt for more information.
##
from Room import Room
from Scenario import Scenario


def test_exit(curr, direction):
    curr = curr.get_exit(direction)
    print("going " + direction)
    print("now in: " + curr.get_description())
    return curr


curr = Scenario.load()
print("testing basics:")
print("name: " + Scenario.name())
print("info: " + Scenario.info())

print("\ntesting all exits:")
print("start: " + curr.get_description())

direction = "south"
curr = test_exit(curr, direction)
print("expected: south america")

direction = "south"
curr = test_exit(curr, direction)
print("expected: antarctica")

direction = "northwest"
curr = test_exit(curr, direction)
print("expected: south america")

direction = "north"
curr = test_exit(curr, direction)
print("expected: north america")

direction = "east"
curr = test_exit(curr, direction)
print("expected: europe")

direction = "south"
curr = test_exit(curr, direction)
print("expected: africa")

direction = "south"
curr = test_exit(curr, direction)
print("expected: antarctica")

direction = "north"
curr = test_exit(curr, direction)
print("expected: africa")

direction = "north"
curr = test_exit(curr, direction)
print("expected: europe")

direction = "east"
curr = test_exit(curr, direction)
print("expected: asia")

direction = "south"
curr = test_exit(curr, direction)
print("expected: australia")

direction = "south"
curr = test_exit(curr, direction)
print("expected: antarctica")

direction = "northeast"
curr = test_exit(curr, direction)
print("expected: australia")

direction = "north"
curr = test_exit(curr, direction)
print("expected: asia")

direction = "east"
curr = test_exit(curr, direction)
print("expected: north america")

direction = "west"
curr = test_exit(curr, direction)
print("expected: asia")

direction = "west"
curr = test_exit(curr, direction)
print("expected: europe")

direction = "west"
curr = test_exit(curr, direction)
print("expected: north america")

direction = "south"
curr = test_exit(curr, direction)
print("expected: south america")

direction = "east"
curr = test_exit(curr, direction)
print("expected: africa")

direction = "east"
curr = test_exit(curr, direction)
print("expected: australia")

direction = "east"
curr = test_exit(curr, direction)
print("expected: south america")

direction = "west"
curr = test_exit(curr, direction)
print("expected: australia")

direction = "west"
curr = test_exit(curr, direction)
print("expected: africa")

direction = "west"
curr = test_exit(curr, direction)
print("expected: south america")
