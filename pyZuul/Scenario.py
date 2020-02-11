##
# Written By Zackery Salzwedel
# This class builds the rooms and exits for an individual scenario the game of zuul.
# Room and exit building is in this class for the default scenario.
# It is inspired by what I remember of Scenario.java
# See project NOTES.txt for more information.
##
from Room import Room


class Scenario:

    @staticmethod
    def name():
        return "default"

    @staticmethod
    def info():
        return "World Map"

    @staticmethod
    def load():
        na = Room("North America")
        sa = Room("South America")
        eu = Room("Europe")
        af = Room("Africa")
        aa = Room("Asia")
        au = Room("Australia")
        ac = Room("Antarctica")

        na.set_exit("west", aa)
        na.set_exit("south", sa)
        na.set_exit("east", eu)
        sa.set_exit("north", na)
        sa.set_exit("west", au)
        sa.set_exit("south", ac)
        sa.set_exit("east", af)
        eu.set_exit("west", na)
        eu.set_exit("south", af)
        eu.set_exit("east", aa)
        af.set_exit("north", eu)
        af.set_exit("west", sa)
        af.set_exit("south", ac)
        af.set_exit("east", au)
        aa.set_exit("west", eu)
        aa.set_exit("south", au)
        aa.set_exit("east", na)
        au.set_exit("north", aa)
        au.set_exit("west", af)
        au.set_exit("south", ac)
        au.set_exit("east", sa)
        ac.set_exit("northwest", sa)
        ac.set_exit("north", af)
        ac.set_exit("northeast", au)

        return na

##
# I think this is the Strategy Pattern.
##
