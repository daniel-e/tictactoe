#!/usr/bin/env python3

# race conditions might exist for concurrent requests

import uuid, threading
from flask import Flask, jsonify, abort

from tictactoe import TicTacToe
from ai import ai_minimax

MAX_ENTRIES = 1000000
store = {}
uids = []

app = Flask(__name__)

def ai(uid):
	t = store[uid]
	if not t.finished():
		x, y = ai_minimax(t)
		t.set(x, y, t.AI)

@app.route("/new", methods = ["POST"])
def new_game():
	uid = str(uuid.uuid4())
	store[uid] = TicTacToe()
	uids.append(uid)
	# limit memory usage
	if len(uids) > MAX_ENTRIES:
		i = uids.pop(0)
		del store[i]
	return jsonify(uid = uid)

@app.route("/status/<string:uid>", methods = ["GET"])
def status(uid):
	if not uid in store:
		abort(404)
	return jsonify(uid = uid, game = store[uid].data())

@app.route("/set/<string:uid>/<int:x>/<int:y>", methods = ["POST"])
def set(uid, x, y):
	if not uid in store:
		abort(404)
	t = store[uid]
	err = "OK"
	try:
		t.set(x, y, t.HUMAN)
		w = threading.Thread(name = "worker", target = ai, args = (uid, ))
		w.start()
	except Exception as e:
		err = str(e)
	return jsonify({"error": err})

if __name__ == "__main__":
	app.run()
