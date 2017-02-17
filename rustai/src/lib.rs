#[macro_use]
extern crate cpython;
use cpython::{Python, PyResult, ToPyObject, PyTuple, PyDict, PythonObject};

mod game;
use game::Game;

// module specific functions

fn minimax(py: Python, d: PyDict) -> PyResult<PyTuple> {

    let ai = try!(d.get_item(py, "ai").unwrap().extract::<i64>(py));
    let human = try!(d.get_item(py, "human").unwrap().extract::<i64>(py));
    let board = try!(d.get_item(py, "board").unwrap().extract::<Vec<i64>>(py));

    let game = Game {
        board: board,
        ai: ai,
        human: human
    };
    let p = game.select_by(ai);
    Ok(PyTuple::new(py,
        &[p.x.into_py_object(py).into_object(), p.y.into_py_object(py).into_object()]
    ))
}

py_module_initializer!(rustai, initai, PyInit_rustai, |py, m| {
    try!(m.add(py, "minimax", py_fn!(py, minimax(d: PyDict))));
    Ok(())
});
