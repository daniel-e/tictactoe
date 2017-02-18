#!/bin/bash

set -e
cd /tmp/
curl https://sh.rustup.rs -sSf | sh -s -- -y
export PATH=$PATH:~/.cargo/bin/
git clone https://github.com/daniel-e/tictactoe.git
cd tictactoe/rustai/
cargo build
echo -e '\033[1;32m'"OK"'\033[0m'
exit 0
