from fabric.api import local, warn
from fabric.colors import green

def docker_compose_up():
    local("docker-compose up")

def webpack():
    local("rm -rf assets/bundles/*")
    local("node_modules/.bin/webpack --config webpack.local.config.js")

def nodejs():
    local('node server.js')

def debug(var=""):

    print(green("--------- debugging ---------"))
    result = local('source venv/bin/activate && ./manage.py runserver {0}'.format(var))
    