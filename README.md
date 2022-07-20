This small app was created in order to provide solutions for the given tasks:
Part 1. Sequence
    The following iterative sequence is defined for the set of positive integers:
    n → n/2 (n is even)
    n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:
13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms.
Assume that all starting numbers eventually finish at 1.

The endpoints:
    \sequence\elem\{n} - Returns the value of the sequence for “n”
    \sequence\longest\{n} - Returns the value smaller than n, that has the longest chain.

Part 2. Iris & pandas
    On service start get iris data set from https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv.
The endpoints:
    \iris\group\sepal_length\{max} - Returns the number of each species with the maximum sepal_length of {max}.
    \iris\describe  - Returns the basic statistics about the columns in data set, like min, max, count, mean etc.

Steps needed to run the application:
After downloading the source code of the app you will need to:
OPTIONAL:
1. Install virtualenv
2. Activate virtualenv
MANDATORY:
1. Install all the needed libraries (after having installed pip)
    pip install -r requirements
3. Type in terminal / command line while in the main app directory (ubs):
    flask run

Testing
While being int the main app directory type in terminal / command line:
    pytest