##
# Written By Zackery Salzwedel
# This file tests the functions of the Scenarios collection class
# See project NOTES.txt for more information.
##
from Scenarios import Scenarios


print("\ntesting scenarios collection functions")
print("list expected: default and simpsons")
print("actual: " + Scenarios.get_scenario_list())

print("\ndefault scene start at expected: North America")
print("actual: " + Scenarios.load_scenario().get_description())

print("\nbad input scene start at expected: North America")
print("actual: " + Scenarios.load_scenario("blearg").get_description())

print("\nsimpsons scene start at expected: Homer")
print("actual: " + Scenarios.load_scenario('family').get_description())
