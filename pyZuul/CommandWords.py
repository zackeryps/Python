##
# Written By Zackery Salzwedel
# This class is a collect of the enumerated commands for Zuul.
# and the functions that support them.
# It is based on CommandWords.java
# See project NOTES.txt for more information.
##
from CommandWord import CommandWord


class CommandWords:
    def __init__(self):
        self._commands = {}  # use a dictionary to collect commands
        for command in CommandWord:
            if command.value != CommandWord.UNKNOWN.value:
                self._commands[command.value] = command

    def is_command(self, command_word):
        if command_word in self._commands.keys():
            return True
        else:
            return False

    def get_command_word(self, command_word):
        if self.is_command(command_word):
            return self._commands[command_word]
        else:
            return CommandWord.UNKNOWN

    def get_string_words(self):
        ret_string = ""
        for command in self._commands.keys():
            ret_string = ret_string + command + " "
        return ret_string

##
# The original .java file had no toString override
# in place there was .showAll() that printed directly to console
# also in the original file was a hashmap for the commands
# it seems the python equivalent is a dict.
##
