from application import app

@app.route('/test')
def tester():
	return 'megasnajs'