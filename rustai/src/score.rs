use position::Position;

#[derive(Clone, Copy)]
pub struct Score {
    pub score: f64,
    pub position: Position
}

impl Score {
    pub fn new(score: f64, position: Position) -> Score {
        Score {
            score: score,
            position: position
        }
    }
}
