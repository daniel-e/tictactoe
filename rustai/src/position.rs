use game::{WIDTH, HEIGHT};

#[derive(PartialEq, Clone, Copy)]
pub struct Position {
    pub x: usize,
    pub y: usize,
}

impl Position {
    pub fn new(x: usize, y: usize) -> Position {
        assert!(x < WIDTH);
        assert!(y < HEIGHT);
        Position {
            x: x,
            y: y
        }
    }
}
