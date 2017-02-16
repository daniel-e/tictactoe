import copy

class TicTacToe():
	EMPTY = 0
	HUMAN = 1
	AI = 2

	STATUS_HUMAN_WON = HUMAN
	STATUS_AI_WON = AI
	STATUS_TURN_HUMAN = 3
	STATUS_TURN_AI = 4
	STATUS_DRAW = 5

	def __init__(self):
		self.w = 3
		self.h = 3
		self.board = [self.EMPTY for i in range(self.w * self.h)]
		self.status = self.STATUS_TURN_HUMAN

	def copy(self):
		return copy.deepcopy(self)

	def status_str(self):
		mapping = {
			self.STATUS_HUMAN_WON: "HUMAN_WINS",
			self.STATUS_AI_WON: "AI_WINS",
			self.STATUS_TURN_AI: "WAITING_FOR_AI",
			self.STATUS_TURN_HUMAN: "WAITING_FOR_HUMAN",
			self.STATUS_DRAW: "DRAW"
		}
		return mapping[self.status]

	def field_str(self):
		mapping = {self.EMPTY: " ", self.HUMAN: "X", self.AI: "O"}
		return [mapping[i] for i in self.board]

	def width(self):
		return self.w

	def height(self):
		return self.h

	def get(self, x, y):
		self._check_input(x, y)
		return self.board[self._pos(x, y)]

	def set(self, x, y, value):
		self._check_input(x, y)
		if value not in [self.HUMAN, self.AI]:
			raise Exception("Invalid value.")
		if self.status in [self.STATUS_AI_WON, self.STATUS_HUMAN_WON, self.STATUS_DRAW]:
			raise Exception("Game already finished.")
		if self.status == self.STATUS_TURN_HUMAN and value != self.HUMAN:
			raise Exception("Invalid player.")
		if self.status == self.STATUS_TURN_AI and value != self.AI:
			raise Exception("Invalid player.")
		if self.get(x, y) != self.EMPTY:
			raise Exception("Invalid move.")

		self.board[self._pos(x, y)] = value
		self._update_status(value)
		return self

	def data(self):
		v = {
			"status": self.status_str(),
			"board": self.field_str()
		}
		return v

	def state(self):
		return self.status

	def finished(self):
		return self.status in [self.STATUS_DRAW, self.STATUS_AI_WON, self.STATUS_HUMAN_WON]

	def empty(self):
		h = range(self.height())
		w = range(self.width())
		return [(x, y) for y in h for x in w if self.get(x, y) == self.EMPTY]

	# ---------------------------------------------------------------------
	# "private" functions
	# ---------------------------------------------------------------------

	def _update_status(self, player):
		if self.status in [self.STATUS_DRAW, self.STATUS_AI_WON, self.STATUS_HUMAN_WON]:
			return
		if self._player_wins(player):
			self.status = player
		elif self._full():
			self.status = self.STATUS_DRAW
		else:
			self.status = self._next_player()

	def _next_player(self):
		h = self.STATUS_TURN_HUMAN
		return self.STATUS_TURN_AI if self.status == h else h

	def _full(self):
		return not any([i == self.EMPTY for i in self.board])

	def _player_wins(self, player):
		mask = [
			[0, 1, 2], [3, 4, 5], [6, 7, 8],
			[0, 3, 6], [1, 4, 7], [2, 5, 8],
			[0, 4, 8], [2, 4, 6]
		]
		for m in mask:
			if all([self.board[i] == player for i in m]):
				return True
		return False

	def _check_input(self, x, y):
		if x < 0 or x >= self.width():
			raise Exception("Invalid coordinates.")
		if y < 0 or y >= self.height():
			raise Exception("Invalid coordinates.")

	def _pos(self, x, y):
		return y * self.width() + x
