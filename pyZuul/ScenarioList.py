##
# Written By Zackery Salzwedel
# This file is a collection of individual scenarios in the game of zuul.
# This file is used to collect scenarios as a map, name -> scenario.
# The Scenarios class hold functions for this collection
# See project NOTES.txt for more information.
##


from Scenario import Scenario
from SimpsonsScenario import SimpsonsScenario


ScenarioList = {
    Scenario.name(): Scenario,
    SimpsonsScenario.name(): SimpsonsScenario
}

##
# Added a properly built subclass of Scenario to this list will automatically add it to the game.
# Based on my understanding of python,
# I could take this further by automating the loading of Scenario classes from an external source such as a folder.
##
