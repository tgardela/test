from app import app

from helpers.helper_functions import is_float
from iris_pandas.iris_pandas import (
    describe,
    sepal_length
)
from sequence.sequence import (
    longest_sequence,
    sequence
)


@app.route('/')
@app.route('/index')
def index():
    return "Solutions of tasks for Python Developer interview."


@app.route('/sequence/elem/<int:number>', methods=['GET'])
def sequence_elem(number):
    return str(sequence(number))


@app.route('/sequence/longest/<int:number>', methods=['GET'])
def sequence_longest(number):
    return str(longest_sequence(number))


@app.route('/iris/group/sepal_length/<string:length>', methods=['GET'])
def iris_sepal_length(length):
    if is_float(length):
        return sepal_length(float(length))
    else:
       return "Provided input is not an int(6) or a float(6.0)"


@app.route('/iris/describe', methods=['GET'])
def iris_describe():
    return describe().to_dict()
