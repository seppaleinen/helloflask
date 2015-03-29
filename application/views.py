import subprocess
from flask import url_for
from application import app

@app.route("/")
def home():
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