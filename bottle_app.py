
# A very simple Bottle Hello World app for you to get started with...
from bottle import default_app, route

@route('/')
def hello_world():
    return 'Hello from Bottle!'
@route('/bye')
def bye_world():
    return 'Bye from Bottle!'

application = default_app()

