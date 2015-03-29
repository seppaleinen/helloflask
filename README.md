<a href='https://coveralls.io/r/seppaleinen/flask?branch=master'><img src='https://coveralls.io/repos/seppaleinen/flask/badge.svg?branch=master' alt='Coverage Status' /></a>

# Flask testapp

#to run server
python runserver.py
 * Running on http://localhost:5000/

#to run tests
python runtests.py

#to run tests with coverage
coverage run --source application runtests.py

#to see coverage result
coverage report -m #For text output
coverage html #For html output

#to install dependencies
pip install -r requirements.txt