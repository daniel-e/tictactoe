# Tic Tac Toe

This is an implementation of the classic game Tic Tac Toe. It consists of a web UI implemented in JavaScript and jQuery and a RESTful web service written in Python using the Flask framework. The RESTful web service manages the games and implements the game engine. The game engine's AI is based on the minimax algorithm which makes the AI unbeatable.

I also created a Python module written in Rust which implements parts of the game engine. It is much faster than the pure Python implementation and is automatically used if the module exists in the appropriate path (see below).

Actually nothing new here. I was just bored.

![tic tac toe screenshot](screenshot.png)

# Setup

The REST service is a standalone Python script which is listening on port 5000 for requests. The web UI is a simple JavaScript application that requires a web server to be delivered. We will configure the web server to listen on port 10000. Furthermore, the web server is used to forward requests to the RESTful web service listening on port 5000. The forwarding is required as due to the same origin policy the JavaScript is not allowed to access responses for requests which are send to a different port.

In the following the steps are described which are required to get Tic Tac Toe running.

## Get the sources

First, we need to get the sources:

```bash
git clone https://github.com/daniel-e/tictactoe.git
cd tictactoe
```

## Install

Type `make` in the directory `tictactoe` to compile and install the Nginx web server into `/opt/nginx/` and the HTML and JavaScript files into `/opt/nginx/tictactoe`. We use the Nginx web server as it is small and easy to configure. Nginx will be configured as follows:

* listen on port 10000
* forward requests to the paths /new, /status, /set to port 5000

# Running Tic Tac Toe

To run Tic Tac Toe start the RESTful web service by typing `./rest.py` in the source directory.

After that start the web server by running `/opt/nginx/sbin/nginx`.

Now, open the URL `http://localhost:10000` in your browser and have fun. :)

# Use Python module written in Rust

To use the Python module written in Rust do the following steps:

```bash
# build the module
cd rustai
cargo build --release
# copy the module to the right location
cp target/release/librustai.so ../rustai.so
cd ..
# start the RESTful service
./rest.py
```
