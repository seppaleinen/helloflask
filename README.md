<a href='https://coveralls.io/r/seppaleinen/flask?branch=master'><img src='https://coveralls.io/repos/seppaleinen/flask/badge.svg?branch=master' alt='Coverage Status' /></a>
<a href="https://codecov.io/github/seppaleinen/flask?branch=master"><img src="https://codecov.io/github/seppaleinen/flask/coverage.svg?branch=master" alt="Coverage via codecov.io" /></a>
<a href="https://landscape.io/github/seppaleinen/flask/master">
  <img alt="Code Health" src="https://landscape.io/github/seppaleinen/flask/master/landscape.svg?style=flat"/></a>

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