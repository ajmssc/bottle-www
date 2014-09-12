from bottle import route, run, template
import happybase

hbase = happybase.Connection('localhost')
my_table = hbase.table('hbase_table')





@route('/')
def index():
	return template('templates/home', title='my site', base='Welcome!')


@route('/api/<key>')
def api(key):
	data = my_table.row(key)
	return data



@route('/hello/<name>')
def hello(name):
	return '<b>Hello %s</b>!' % name








run(host='0.0.0.0', port=8080)