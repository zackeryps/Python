##
# Written By Zackery Salzwedel
# This class is a collection functions for individual scenarios in the game of zuul.
# Function logic logic is in this class.
# It is based what I learned in CST276 'Software Design Patterns'
# See project NOTES.txt for more information.
##
from ScenarioList import ScenarioList
from Scenario import Scenario


class Scenarios:

    @staticmethod
    def get_scenario_list():
        ret_str = ""
        for scene in ScenarioList.keys():
            ret_str = ret_str + "\n" + ScenarioList[scene].name() + ": " + ScenarioList[scene].info()
        return ret_str

    @staticmethod
    def load_scenario(name=None):
        if name in ScenarioList.keys():
            return ScenarioList[name].load()
        else:
            return Scenario.load()

##
# I think this is the Strategy Pattern.
##
