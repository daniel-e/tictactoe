import random
from collections import namedtuple

Score = namedtuple("Score", "score, move")

def _score(board):
	if board.state() == board.STATUS_AI_WON:
		return 1.0
	if board.state() == board.STATUS_HUMAN_WON:
		return -1.0
	return 0.0

def _min_max(l, min_max_func):
	x = min_max_func(l)
	return random.choice([i for i in l if i.score == x.score])

def _ai_minimax(t, move, player):
	b = t.copy().set(move[0], move[1], player)
	if b.finished():
		return _score(b)
	if player == t.AI:
		return _select_by(b, t.HUMAN, min).score
	else:
		return _select_by(b, t.AI, max).score

def _select_by(b, player, f):
	return _min_max([Score(_ai_minimax(b, i, player), i) for i in b.empty()], f)

def ai_minimax(t):
	return _select_by(t, t.AI, max).move
