use game::{Game, AI, HUMAN, STATUS_AI_WON, STATUS_HUMAN_WON};
use position::Position;
use score::Score;
use rand::{Rng, thread_rng};

pub fn minimax(game: Game) -> Position {
    _select_by(game, AI).position
}

fn _score(game: Game) -> f64 {
    match game.state() {
        STATUS_AI_WON    =>  1.0,
        STATUS_HUMAN_WON => -1.0,
        _ => 0.0
    }
}

fn _ai_minimax(game: &Game, p: Position, player: i64) -> f64 {

    let g = game.set(p, player);

    match g.finished() {
        true => _score(g),
        _    => match player {
            AI => _select_by(g, HUMAN),
            _  => _select_by(g, AI), /* human */
        }.score
    }
}

fn _select_by(game: Game, player: i64) -> Score {

    // Compute the score for each valid move.
    let scores = game.empty()
        .iter().map(|&p| Score::new(_ai_minimax(&game, p, player), p)).collect::<Vec<_>>();

    // Search the maximum/minimum score depending on the player.
    let x = match player {
        AI => scores.iter().max_by(|x, y| x.score.partial_cmp(&y.score).unwrap()).unwrap(),
        _  => scores.iter().min_by(|x, y| x.score.partial_cmp(&y.score).unwrap()).unwrap() /* human */
    };

    // Select a move at random among the maximums/minimums.
    **thread_rng().choose(&scores.iter()
        .filter(|s| s.score == x.score).collect::<Vec<_>>()).unwrap()
}
