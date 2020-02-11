##
# Written By Zackery Salzwedel
# This file is unit tests for the functions of the Scenarios collection class
# See project NOTES.txt for more information.
##
import unittest
from Scenarios import Scenarios


class MyTestCase(unittest.TestCase):
    def test_list_all(self):
        expected = ""
        expected += "\ndefault: World Map"
        expected += "\nfamily: Simpson's Family Tree"
        self.assertEqual(Scenarios.get_scenario_list(), expected)

    def test_no_input(self):
        self.assertEqual(Scenarios.load_scenario().get_description(), "North America")

    def test_bad_input(self):
        self.assertEqual(Scenarios.load_scenario("blearg").get_description(), "North America")

    def test_family_input(self):
        self.assertEqual(Scenarios.load_scenario("family").get_description(), "Homer")


if __name__ == '__main__':
    unittest.main()
