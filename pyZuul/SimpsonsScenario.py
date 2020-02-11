##
# Written By Zackery Salzwedel
# This class builds the rooms and exits for an individual scenario the game of zuul.
# Room and exit building is in this class for a special scenario: Simpson's family tree.
# It is based what I learned in CST276 'Software Design Patterns'
# See project NOTES.txt for more information.
##
from Room import Room
from Scenario import Scenario


class SimpsonsScenario(Scenario):

    @staticmethod
    def name():
        return "family"

    @staticmethod
    def info():
        return "Simpson's Family Tree"

    @staticmethod
    def load():
        abe = Room("Abraham")
        clancy = Room("Clancy")
        herb = Room("Herb")
        homer = Room("Homer")
        bart = Room("Bart")
        mona = Room("Mona")
        jackie = Room("Jackie")
        marge = Room("Marge")
        patty = Room("Patty")
        selma = Room("Selma")
        lisa = Room("Lisa")
        maggie = Room("Maggie")
        ling = Room("Ling")

        abe.set_exit("son1", herb)
        abe.set_exit("son2", homer)

        mona.set_exit("son1", herb)
        mona.set_exit("son2", homer)

        clancy.set_exit("daughter1", marge)
        clancy.set_exit("daughter2", patty)
        clancy.set_exit("daughter3", selma)

        jackie.set_exit("daughter1", marge)
        jackie.set_exit("daughter2", patty)
        jackie.set_exit("daughter3", selma)

        herb.set_exit("father", abe)
        herb.set_exit("mother", mona)

        homer.set_exit("father", abe)
        homer.set_exit("mother", mona)
        homer.set_exit("son", bart)
        homer.set_exit("daughter1", lisa)
        homer.set_exit("daughter2", maggie)

        marge.set_exit("father", clancy)
        marge.set_exit("mother", jackie)
        marge.set_exit("son", bart)
        marge.set_exit("daughter1", lisa)
        marge.set_exit("daughter2", maggie)

        patty.set_exit("father", clancy)
        patty.set_exit("mother", jackie)

        selma.set_exit("father", clancy)
        selma.set_exit("mother", jackie)
        selma.set_exit("daughter", ling)

        bart.set_exit("father", homer)
        bart.set_exit("mother", marge)

        lisa.set_exit("father", homer)
        lisa.set_exit("mother", marge)

        maggie.set_exit("father", homer)
        maggie.set_exit("mother", marge)

        ling.set_exit("mother", selma)

        return homer

##
# I think this is the Strategy Pattern.
##
