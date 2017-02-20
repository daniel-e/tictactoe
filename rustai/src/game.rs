pub const EMPTY: i64 = 0;
pub const HUMAN: i64 = 1;
pub const AI: i64 = 2;

pub const STATUS_HUMAN_WON: i64 = HUMAN;
pub const STATUS_AI_WON: i64 = AI;
pub const STATUS_TURN_HUMAN: i64 = 3;
pub const STATUS_TURN_AI: i64 = 4;
pub const STATUS_DRAW: i64 = 5;

pub const WIDTH: usize = 3;
pub const HEIGHT: usize = 3;

use position::Position;

#[derive(Clone)]
pub struct Game {
    pub board: Vec<i64>,
    pub status: i64
}

// Implements only a subset of the class TicTacToe in tictactoe.py
impl Game {
    pub fn state(&self) -> i64 {
        self.status
    }

    pub fn finished(&self) -> bool {
        self.status == STATUS_DRAW || self.status == STATUS_AI_WON || self.status == STATUS_HUMAN_WON
    }

    pub fn empty(&self) -> Vec<Position> {
        (0..self.board.len())
            .filter(|&x| self.board[x] == 0).map(|x| Game::position_for_idx(x)).collect()
    }

    fn position_for_idx(idx: usize) -> Position {
        Position::new(idx % WIDTH, idx / HEIGHT)
    }

    pub fn set(&self, p: Position, player: i64) -> Self {
        let mut v = self.board.to_vec();
        let s = v.as_mut_slice();
        s[p.y * WIDTH + p.x] = player;

        let g = Game {
            board: s.to_vec(),
            status: self.status
        };
        let n = g.new_status(player);

        Game {
            board: g.board,
            status: n
        }
    }

    fn new_status(&self, player: i64) -> i64 {
        if self.finished() {
            return self.state();
        } else if self.player_wins(player) {
            return player;
        } else if self.full() {
            return STATUS_DRAW;
        } else {
            self.next_player()
        }
    }

    fn full(&self) -> bool {
        self.board.iter().all(|&x| x != EMPTY)
    }

    fn player_wins(&self, player: i64) -> bool {
        vec![
            [0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7],
            [2, 5, 8], [0, 4, 8], [2, 4, 6]
        ].iter().any(|k| k.iter().all(|&x| self.board[x] == player))
    }

    fn next_player(&self) -> i64 {
        match self.status {
            STATUS_TURN_AI => STATUS_TURN_HUMAN,
            _              => STATUS_TURN_AI
        }
    }
}

// -----------------------------------------------------------------------------------------------
// TESTS
// -----------------------------------------------------------------------------------------------

#[cfg(test)]
mod tests {
    use game::{Game, STATUS_TURN_HUMAN, STATUS_DRAW, STATUS_AI_WON, STATUS_HUMAN_WON, AI, HUMAN, EMPTY};
    use position::Position;
    use std::iter::repeat;

    fn new_game() -> Game {
        Game {
            board: repeat(EMPTY).take(9).collect(),
            status: STATUS_TURN_HUMAN
        }
    }

    #[test]
    fn test_position() {
        let p = Position::new(1, 2);
        assert!(p.x == 1);
        assert!(p.y == 2);
    }

    #[test]
    fn test_position_for_idx() {
        assert!(Game::position_for_idx(1) == Position { x: 1, y: 0});
        assert!(Game::position_for_idx(5) == Position { x: 2, y: 1});
    }

    #[test]
    fn test_new() {
        let g = new_game();
        assert!(g.clone().state() == STATUS_TURN_HUMAN);
        assert!(g.clone().empty().len() == 9);
    }

    fn create_game(status: i64) -> Game {
        Game {
            board: vec![0],
            status: status
        }
    }

    #[test]
    fn test_finished() {
        assert!(create_game(STATUS_DRAW).finished() == true);
        assert!(create_game(STATUS_HUMAN_WON).finished() == true);
        assert!(create_game(STATUS_AI_WON).finished() == true);
    }

    #[test]
    fn test_set() {
        let v = new_game()
            .set(Position::new(1, 2), AI)
            .set(Position::new(0, 0), HUMAN)
            .set(Position::new(2, 2), AI)
            .set(Position::new(0, 2), HUMAN)
            .set(Position::new(1, 1), AI)
            .empty().iter().map(|p| (p.x, p.y)).collect::<Vec<_>>();
        assert!(v == vec![(1, 0), (2, 0), (0, 1), (2, 1)]);
    }
}
