from fabric.api import local, warn, env
from fabric.colors import green, red

def run_with_venv(command, capture=True):
    env.warn_only = True
    result = local('source venv/bin/activate && {}'.format(command), capture=capture)
    if result.stderr:
        print result.stderr
        print red("--------- ERROR ---------")
    else:
        print green("--------- successfully completed ---------")

def requirements(local=True):
    command = "pip install -r requirements/base.txt"
    if local:
        command += " && pip install -r requirements/local.txt"
    run_with_venv(command)

def webpack():
    local("rm -rf assets/bundles/*")
    local("node_modules/.bin/webpack --config webpack/local.config.js")

def nodejs():
    local('node server.js')

def celery():
    run_with_venv('celery -A _game_chats worker -l info -Q user_tasks_queue', capture=False)

def debug(var=""):
    run_with_venv("./manage.py runserver {0}".format(var), capture=False)
    