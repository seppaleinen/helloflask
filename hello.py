from flask import Flask, url_for
app = Flask(__name__)
#To turn off debugging
app.debug = False

@app.route("/")
def hello():
    return "Hello World!"

@app.route('/user/<user>')
def show_user(user):
    return 'User %s' % user

@app.route('/post_id/<int:post_id>')
def show_post(post_id):
    return 'Post %d' % post_id

@app.route('/post', methods=['POST'])
def post():
    return 'POST'

#with app.test_request_context():
#    print url_for('hello')

if __name__ == "__main__":
    #Enable listen to all public IP
    app.run(host='0.0.0.0')
    #app.run()