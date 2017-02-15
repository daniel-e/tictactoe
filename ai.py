import random

def _score(board):
	if board.state() == board.STATUS_AI_WON:
		return 1.0
	if board.state() == board.STATUS_HUMAN_WON:
		return -1.0
	return 0.0

def _select_random_max_min(l, min_max_func):
	x = min_max_func(l)
	return random.choice([i for i in l if i[0] == x[0]])

def _ai_minimax(t, player):
	scores = []
	if player == t.AI:
		for x, y in t.empty(): # iterate over all possible moves
			b = t.copy().set(x, y, player)
			# terminal node
			if b.finished():
				return [_score(b), (x, y)]
			score, move = _ai_minimax(b, t.HUMAN)
			scores.append((score, (x, y)))
		v =_select_random_max_min(scores, max)
		return [v[0], v[1]]
	if player == t.HUMAN:
		for x, y in t.empty(): # iterate over all possible moves
			b = t.copy().set(x, y, player)
			# terminal node
			if b.finished():
				return [_score(b), (x, y)]
			score, move = _ai_minimax(b, t.AI)
			scores.append((score, (x, y)))
		v = _select_random_max_min(scores, min)
		return [v[0], v[1]]

def ai_minimax(t):
	score, move = _ai_minimax(t, t.AI)
	return move
