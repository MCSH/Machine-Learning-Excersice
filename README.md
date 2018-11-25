# Machine Learning Excersice

## Project structure

The `inputs` folder should contain the datasets. The `predictor` model contains the python script to apply a trained model on data inside a database, as provided by `db.py`. The main notebook is located at `project.ipynb` and a trained model is pickled at `model.pkl`.

## Jupyter notebook

The jupyter notebook is self explanetory, it is well commented and the markdown cell blocks explain everything.

## Predictor Script

The predictor script has two files: `main.py` load the model and applies it to a database, provided by `db.py`. As of this version `db.py` relies on sqlite3, however that is not a requirement. Any other database could be used as long as the class provides the following methods:

* `read` should return a generator of the data, each given as a tuple conssisting of id and an array that holds the input.

* `write(id, target)` should write the results back to the database

# Requirements

Python 3 with the following modules are required in order to run this project:

* sklearn
* numpy
* matplotlib

