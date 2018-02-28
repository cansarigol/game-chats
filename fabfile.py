from fabric.api import local

def docker_compose_up():
    local("docker-compose up")

def webpack():
    local("rm -rf assets/bundles/*")
    local("node_modules/.bin/webpack --config webpack.local.config.js")