##
# Written By Zackery Salzwedel
# This class is the commands for Zuul,
# and the functions that support them.
# It is based on Command.java
# See project NOTES.txt for more information.
##
from CommandWord import CommandWord
from CommandWords import CommandWords


class Command:
    def __init__(self, command, second=None):
        if CommandWords.is_command(CommandWords(), command):  # call the function like a static function using a new...
            self._command_word = CommandWords.get_command_word(CommandWords(), command)  #  ...CommandWords instance
        elif command in CommandWord:
            self._command_word = command
        else:
            self._command_word = CommandWord.UNKNOWN
        self._second_word = second

    def get_command_word(self):
        return self._command_word

    def get_second_word(self):
        return self._second_word

    def has_second_word(self):
        return self.get_second_word() is not None

    def is_unknown(self):
        return self.get_command_word() == CommandWord.UNKNOWN

##
# The getters aren't required since python doesn't have private data members,
# however they have been included and use for completeness and ease of expansion.
# The original .java file did not type-validate the incoming command_word here,
# but in the Parser.java class instead.
# This change was made for python because java enforced the datatype of the parameter as CommandWord.
##
