from high_score import *
import unittest



class TestStringMethods(unittest.TestCase):

	def test_gameboard(self):
		entry = Gameboard('madhur',10)
		self.assertEqual(entry.get_name(),'madhur')
		self.assertEqual(entry.get_score(),10)

	def test_scoreboard(self):
		board = Scoreboard(capacity=1)
		entry = Gameboard('madhur',10)
		board.add(entry)
		self.assertEqual(board.get_capacity(),1)
	   

if __name__ == '__main__':
	unittest.main()