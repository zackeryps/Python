##
# Written By Zackery Salzwedel
# This class is takes input from the user
# and converts it into a Zuul command.
# It is based on Parser.java
# See project NOTES.txt for more information.
##
from CommandWords import CommandWords
from Command import Command


class Parser:
    @staticmethod
    def parse_command(inp=None):
        if inp is None:
            input_raw = input("Parse a command: ").lower()
        else:
            input_raw = inp.lower()

        if input_raw.find(" ") != -1:
            input_words = input_raw.split(" ")
            return Command(input_words[0], input_words[1])
        else:
            return Command(input_raw)

    @staticmethod
    def string_commands():
        return CommandWords.get_string_words(CommandWords())

##
# The original .java source had a call to CommandWords.getCommandWords()
# and an instance variable of type CommandWords to call it from.
# Moved the type-checking into the Command class (done at instantiation).
# Converted all class methods to static methods and removed instance variables.
##
