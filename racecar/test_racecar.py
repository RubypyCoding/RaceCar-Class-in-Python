import unittest
from racecar import *


class RaceCarTests(unittest.TestCase):

	def setUp(self):
		self.car1 = RaceCar({"name": "Force", "lap_times": [10.45, 10.44, 10.38, 10.58, 10.78]})
		self.car2 = RaceCar({"name": "Power", "lap_times": [8.45, 8.44, 7.38, 8.58, 8.78]})
		self.car3 = RaceCar({"name": "Passwater", "lap_times": [9.45, 9.24, 9.38, 9.68, 9.21]})


	def test_name_is_evaluated_as_getter(self):
	    self.assertEqual(self.car1.name, "Force")

	def test_name_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
		    self.car1.name = "Forzy"

	def test_lap_times_is_evaluated_as_getter(self):
		raised = False
		try:
			self.car1.lap_times
		except:
			raised = True
		self.assertFalse(raised, "Exception raised")

	def test_lap_times_is_evaluated_as_setter(self):
		raised = False
		try:
			self.car1.lap_times = [8.45, 8.44, 7.38, 8.58, 8.78]
		except:
			raised = True
		self.assertFalse(raised, "Exception raised")

	def test_average_speed_if_average_speed_returns_a_string_with_average_of_speed(self):
		self.assertEqual(self.car1.average_speed(), 9.5)
		self.assertEqual(self.car3.average_speed(), 10.65)

	def test_status_if_status_returns_level_of_racecar(self):
		self.assertEqual(self.car2.status(), "Medio")

	def test_status_if_status_returns_message_when_there_is_no_level_of_racecar_for_average_speed(self):
		self.car1.lap_times = [2, 2, 2, 2, 2]
		self.assertEqual(self.car1.status(), "No status")


class TeamTests(unittest.TestCase):

	def setUp(self):
		self.car1 = RaceCar({"name": "Force", "lap_times": [10.45, 10.44, 10.38, 10.58, 10.78]})
		self.car2 = RaceCar({"name": "Power", "lap_times": [8.45, 8.44, 7.38, 8.58, 8.78]})
		self.car3 = RaceCar({"name": "Passwater", "lap_times": [9.45, 9.24, 9.38, 9.68, 9.21]})
		self.car4 = RaceCar({"name": "Banjo", "lap_times": [9.02, 9.10, 9.12, 9.09, 9.14]})
		self.car5 = RaceCar({"name": "Duck", "lap_times": [10.02, 9.90, 10.12, 9.50, 9.70]})
		self.car6 = RaceCar({"name": "CooCoo", "lap_times": [7.02, 5.90, 4.12, 6.50, 8.70]})
		self.team1 = [self.car1, self.car2, self.car3, self.car4, self.car5]
		self.team_one = Team(self.team1)

	def test_team_team_is_evaluated_as_getter(self):
		raised = False
		try:
			self.team_one.team
		except:
			raised = True
		self.assertFalse(raised, "Exception raised")

	def test_team_team_is_evaluated_as_setter(self):
		with self.assertRaises(AttributeError):
			self.team_one.team = self.car6

	def test_add_if_add_inserts_a_new_racecar_object_in_team(self):
		self.assertEqual(len(self.team_one.team), 5)
		raised = False
		try:
			self.team_one.add(self.car6)
		except:
			raised = True
		self.assertFalse(raised, "Exception raised")
		self.assertEqual(len(self.team_one.team), 6)

	def test_average_speed_of_team_if_average_speed_of_team_calculates_average_speed_of_team(self):
		self.assertEqual(self.team_one.average_speed_of_team(), 10.66)


class SearchTests(unittest.TestCase):

	def setUp(self):
		self.car1 = RaceCar({"name": "Force", "lap_times": [10.45, 10.44, 10.38, 10.58, 10.78]})
		self.car2 = RaceCar({"name": "Power", "lap_times": [8.45, 8.44, 7.38, 8.58, 8.78]})
		self.team1 = [self.car1, self.car2]
		self.team_one = Team(self.team1)

	def test_search_if_search_finds_racecar_in_team(self):
		self.assertEqual(search("Power", self.team_one), "Power is a racer")

	def test_search_if_search_not_finds_racecar_in_team(self):
		self.assertEqual(search("Duck", self.team_one), "Duck is not a racer")



if __name__=="__main__":
    unittest.main()