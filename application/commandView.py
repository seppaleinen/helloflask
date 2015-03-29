from application import app

@app.route('/command/remove_torrent', methods=['POST'])
def remove_torrent():
    cmd = 'find ~/Downloads -mindepth 1 -maxdepth 1 -type f -name *.torrent -exec rm -f {} \;'
    return __run_subprocess__(cmd)

@app.route('/command/remove_trash', methods=['POST'])
def remove_trash():
    cmd = 'find ~/.Trash -mindepth 1 -maxdepth 1 -exec rm -rf {} \;'
    return __run_subprocess__(cmd)

@app.route('/command/update_git', methods=['POST'])
def update_git():
    cmd = "find ~/IdeaProjects -mindepth 2 -maxdepth 2 -type d -name .git -exec sh -c 'TREE=$( echo {} | sed 's_/\.git__g' ); git --git-dir={} --work-tree=$TREE pull' \;"
    return __run_subprocess__(cmd)

def __run_subprocess__(cmd):
    if not app.config['TESTING']:
        result = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE).stdout.read()
    else:
        result = cmd
    return result