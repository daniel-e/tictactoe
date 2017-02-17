pub struct Game {
    pub board: Vec<i64>,
    pub ai: i64,
    pub human: i64,
}

#[derive(PartialEq)]
pub struct Position {
    pub x: usize,
    pub y: usize,
}

pub struct Score {
    score: f64,
    position: Position
}


impl Position {
    fn new(x: usize, y: usize) -> Position {
        Position {
            x: x,
            y: y
        }
    }
}

impl Game {
    pub fn select_by(self, player: i64) -> Position {
        Position { x: 1, y: 2 }
    }

    fn set(self, p: Position, player: i64) -> Self {
        let mut v = self.board.to_vec();
        let s = v.as_mut_slice();
        s[p.y * 3 + p.x] = player;
        Game {
            board: s.to_vec(),
            ai: self.ai,
            human: self.human
        }
    }

    fn empty(self) -> Vec<Position> {
        self.board.iter().enumerate()
            .filter(|&(idx, val)| *val == 0).map(|(idx, _)| idx)
            .map(|idx| Game::position_for_idx(idx))
            .collect()
    }

    fn position_for_idx(idx: usize) -> Position {
        Position {
            x: idx % 3,
            y: idx / 3,
        }
    }
}

#[cfg(test)]
mod tests {
    use game::Game;
    use game::Position;

    #[test]
    fn game_position_for_idx() {
        assert!(Game::position_for_idx(1) == Position { x: 1, y: 0});
        assert!(Game::position_for_idx(5) == Position { x: 2, y: 1});
    }

    #[test]
    fn set() {
        //let g = Game::new().set(0, 0, 1)
    }
}
