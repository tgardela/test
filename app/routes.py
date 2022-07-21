from app import app

from helpers.helper_functions import is_float
from iris_pandas.iris_pandas import (
    describe,
    get_values_less_than
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


# By changing the 'sepal_length' part of endpoint url to '<string: value_type>' we can get an endpoint that would be
# able to return values for all types of iris dimensions although some additional verification of the 'value_type'
# parameter should be also done (like for 'length'). As this was not the part of the task I did not implement it.
@app.route('/iris/group/sepal_length/<string:length>', methods=['GET'])
def iris_sepal_length(length):
    if is_float(length):
        return get_values_less_than(float(length), 'sepal_length')
    else:
       return "Provided input is not an int(6) or a float(6.0)"


@app.route('/iris/describe', methods=['GET'])
def iris_describe():
    return describe().to_dict()
