from flask import Flask, url_for
import subprocess

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

@app.route('/command/<cmd>', methods=['POST'])
def command(cmd):
    if 'torrent' in cmd:
        cmd = 'find ~/Downloads -mindepth 1 -maxdepth 1 -type f -name *.torrent -exec rm -f {} \;'
    elif 'trash' in cmd:
        cmd = 'find ~/.Trash -mindepth 1 -maxdepth 1 -exec rm -rf {} \;'
    elif 'git' in cmd:
        cmd = "find ~/IdeaProjects -mindepth 2 -maxdepth 2 -type d -name .git -exec sh -c 'TREE=$( echo {} | sed 's_/\.git__g' ); git --git-dir={} --work-tree=$TREE pull' \;"
    else:
        return 'Not a valid command'
        
    result = None
    if not app.config['TESTING']:
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    else:
        result = 'test'
    return result

#with app.test_request_context():
#    print url_for('hello')

if __name__ == "__main__":
    #Enable listen to all public IP
    app.run(host='0.0.0.0')
    #app.run()