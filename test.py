#!/usr/bin/env python3

import unittest

from tictactoe import TicTacToe
import ai

class BoardTest(unittest.TestCase):
	def test_constructor(self):
		t = TicTacToe()
		self.assertEqual(t.board, [0, 0, 0, 0, 0, 0, 0, 0, 0])
		self.assertEqual(t.status, t.STATUS_TURN_HUMAN)
		self.assertEqual(t.width(), 3)
		self.assertEqual(t.height(), 3)

	def test_get(self):
		t = TicTacToe()
		for y in range(3):
			for x in range(3):
				self.assertEqual(t.get(x, y), t.EMPTY)
		t.board[1] = t.AI
		self.assertEqual(t.get(1, 0), t.AI)
		t.board[5] = t.HUMAN
		self.assertEqual(t.get(2, 1), t.HUMAN)
		self.assertRaises(Exception, t.get, *[3, 0])
		self.assertRaises(Exception, t.get, *[0, 3])
		self.assertRaises(Exception, t.get, *[-1, 0])
		self.assertRaises(Exception, t.get, *[0, -1])

	def test_set(self):
		t = TicTacToe()
		# check range for parameter value
		# invalid value exception
		self.assertRaises(Exception, t.set, *[0, 0, 0])
		self.assertRaises(Exception, t.set, *[0, 0, 3])
		t.set(1, 0, t.HUMAN)
		# invalid player exception
		self.assertRaises(Exception, t.set, *[2, 0, t.HUMAN])
		t.set(0, 0, t.AI)
		# invalid move exception
		self.assertRaises(Exception, t.set, *[1, 0, t.HUMAN])
		t.set(0, 1, t.HUMAN)

	def test_next_player(self):
		t = TicTacToe()
		self.assertEqual(t.state(), t.STATUS_TURN_HUMAN)
		t.status = t._next_player()
		self.assertEqual(t.state(), t.STATUS_TURN_AI)
		t.status = t._next_player()
		self.assertEqual(t.state(), t.STATUS_TURN_HUMAN)

	def test_full(self):
		t = TicTacToe()
		self.assertFalse(t._full())
		t.board = [1, 1, 1, 1, 1, 1, 1, 1, 1]
		self.assertTrue(t._full())

	def test_player_wins(self):
		t = TicTacToe()
		self.assertFalse(t._player_wins(t.HUMAN))
		self.assertFalse(t._player_wins(t.AI))
		t.set(0, 0, t.HUMAN).set(0, 1, t.AI).set(1, 0, t.HUMAN).set(1, 1, t.AI)
		self.assertFalse(t._player_wins(t.HUMAN))
		self.assertFalse(t._player_wins(t.AI))
		t.set(2, 0, t.HUMAN)
		self.assertTrue(t._player_wins(t.HUMAN))
		# already finished exception
		self.assertRaises(Exception, t.set, *[2, 1, t.AI])

	def test_player_wins_2(self):
		t = TicTacToe()
		h = t.HUMAN
		t.board = [h, h, h, 0, 0, 0, 0, 0, 0]
		self.assertTrue(t._player_wins(h))
		t.board = [0, 0, 0, h, h, h, 0, 0, 0]
		self.assertTrue(t._player_wins(h))
		t.board = [0, 0, 0, 0, 0, 0, h, h, h]
		self.assertTrue(t._player_wins(h))

		t.board = [h, 0, 0, h, 0, 0, h, 0, 0]
		self.assertTrue(t._player_wins(h))
		t.board = [0, h, 0, 0, h, 0, 0, h, 0]
		self.assertTrue(t._player_wins(h))
		t.board = [0, 0, h, 0, 0, h, 0, 0, h]
		self.assertTrue(t._player_wins(h))

		# diagonals
		t.board = [h, 0, 0, 0, h, 0, 0, 0, h]
		self.assertTrue(t._player_wins(h))
		t.board = [0, 0, h, 0, h, 0, h, 0, 0]
		self.assertTrue(t._player_wins(h))

	def test_empty(self):
		t = TicTacToe()
		t.board = [0, 0, 1, 1, 1, 1, 1, 1, 0]
		self.assertEqual(t.empty(), [(0, 0), (1, 0), (2, 2)])

	def test_copy(self):
		t = TicTacToe()
		x = t.copy()
		x.board[1] = 1
		self.assertEqual(t.board[1], 0)

if __name__ == "__main__":
	unittest.main()
