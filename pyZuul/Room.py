##
# Written By Zackery Salzwedel
# This class models a room of zuul
# and the functions that support it.
# It is based on Room.java
# See project NOTES.txt for more information.
##


class Room:
    def __init__(self, description):
        self._description = description
        self._exits = {}

    def get_description(self):
        return self._description

    def get_exits_string(self):
        ret_string = ""
        for direction in self._exits.keys():
            ret_string = ret_string + direction + " "
        return ret_string

    def get_description_verbose(self):
        return "Thing: " + self._description + " Paths: " + self.get_exits_string()

    def set_exit(self, direction, neighbor):
        self._exits[direction.lower()] = neighbor

    def get_exit(self, direction):
        if direction in self._exits.keys():
            return self._exits[direction]
        else:
            return None

##
# The original .java file used a hashmap for the exits.
# It seems the python equivalent is a dict.
##
