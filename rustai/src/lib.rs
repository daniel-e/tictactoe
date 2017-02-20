#[macro_use]
extern crate cpython;
extern crate rand;
use cpython::{Python, PyResult, ToPyObject, PyTuple, PyDict, PythonObject};

mod game;
mod ai;
mod position;
mod score;

fn minimax(py: Python, d: PyDict) -> PyResult<PyTuple> {

    let g = game::Game {
        board: try!(d.get_item(py, "board").unwrap().extract::<Vec<i64>>(py)),
        status: game::STATUS_TURN_AI
    };

    let p = ai::minimax(g);

    Ok(PyTuple::new(py,
        &[p.x.into_py_object(py).into_object(), p.y.into_py_object(py).into_object()]
    ))
}

py_module_initializer!(rustai, initai, PyInit_rustai, |py, m| {
    try!(m.add(py, "minimax", py_fn!(py, minimax(d: PyDict))));
    Ok(())
});
