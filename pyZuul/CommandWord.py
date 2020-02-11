##
# Written By Zackery Salzwedel
# This class is the enumerated commands for Zuul.
# It is based on CommandWord.java
# See project NOTES.txt for more information.
##
from enum import Enum


class CommandWord(Enum):
    GO = "go"
    QUIT = "quit"
    HELP = "help"
    UNKNOWN = "unknown"

##
# enum values can be accessed via .value
# e.g CommandWord.GO.value == "go" is true
# as a result, the additional logic present in the original .java file is already present
##
