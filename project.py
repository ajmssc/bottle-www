from bottle import route, run, template

@route('/')
def index():
	return template('templates/home', title='my site', base='Welcome!')


@route('/hello/<name>')
def hello(name):
    return '<b>Hello %s</b>!' % name

run(host='0.0.0.0', port=8080)