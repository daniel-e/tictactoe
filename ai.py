import random, functools

def ai_random(t):
	return random.choice(t.empty())

@functools.lru_cache(maxsize = None, typed = True)
def _ai_minimax(t, player):
	if player == t.AI:
		scores = []
		for x, y in t.empty(): # iterate over all possible moves
			b = t.copy()
			b.set(x, y, player)
			# terminal node
			if b.state() == b.STATUS_AI_WON:
				return [1.0, (x, y)]
			elif b.state() == b.STATUS_DRAW:
				return [0.0, (x, y)]
			score, move = _ai_minimax(b, t.HUMAN)
			scores.append((score, (x, y)))
		v = max(scores)
		return [v[0], v[1]]
	if player == t.HUMAN:
		scores = []
		for x, y in t.empty(): # iterate over all possible moves
			b = t.copy()
			b.set(x, y, player)
			# terminal node
			if b.state() == b.STATUS_HUMAN_WON:
				return [-1.0, (x, y)]
			elif b.state() == b.STATUS_DRAW:
				return [0.0, (x, y)]
			score, move = _ai_minimax(b, t.AI)
			scores.append((score, (x, y)))
		v = min(scores)
		return [v[0], v[1]]

def ai_minimax(t):
	score, move = _ai_minimax(t, t.AI)
	return move
