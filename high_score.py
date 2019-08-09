class Gameboard:
	def __init__(self,name,score):
		self._name = name
		self._score = score

	def get_score(self):
		return self._score

	def __str__(self):
		return f'({self._name},(self._score))'
	def get_name(self):
		return self._name

class Scoreboard:
	def __init__(self, capacity=10):
		self._n= 0
		self._board = capacity *[None]

	def add(self,entry):
		score = entry.get_score()
		good =  self._n < len(self._board) or score > self._board[-1].get_score
		
		if good:
			if self._n < len(self._board):
				self._n+=1

			j = self._n -1
			while j>0 and self._board[j-1] < score:
				self._board[j] = self._board[j-1]
				j-=1
			self._board[j] = entry

	def get_capacity(self):
		return len(self._board)