<a href='https://coveralls.io/r/seppaleinen/flask?branch=master'><img src='https://coveralls.io/repos/seppaleinen/flask/badge.svg?branch=master' alt='Coverage Status' /></a>
<a href="https://codecov.io/github/seppaleinen/flask?branch=master"><img src="https://codecov.io/github/seppaleinen/flask/coverage.svg?branch=master" alt="Coverage via codecov.io" /></a>
<a href="https://landscape.io/github/seppaleinen/flask/master">
  <img alt="Code Health" src="https://landscape.io/github/seppaleinen/flask/master/landscape.svg?style=flat"/></a>
<img src="https://travis-ci.org/seppaleinen/flask.svg" data-bindattr-817="817" title="Build Status Images">
<a href="https://requires.io/github/seppaleinen/flask/requirements/?branch=master"><img src="https://requires.io/github/seppaleinen/flask/requirements.svg?branch=master" alt="Requirements Status" /></a>

#Flask testapp

###To run flask server running on localhost:5000
`
python runserver.py
`

###To start gunicorn server running on localhost:8000
`
gunicorn --config=gunicorn.config.py wsgi:app
`

###To run tests
`
python runtests.py
`

###To run tests with coverage
`
coverage run --source application runtests.py
`

###To see coverage result

`coverage report -m ` For text output
`coverage html` For html output

###To install dependencies
`
pip install -r requirements.txt
