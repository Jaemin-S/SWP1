from cgi import parse_qs
from template import html

def application(environ, start_response):
        d = parse_qs(environ['QUERY_STRING'])
        a = d.get('a', [''])[0]
        b = d.get('b', [''])[0]
	x = 0
	y = 0
	try:
                a, b = int(a), int(b)
                x = a + b
                y = a * b
		x, y = str(x), str(y)
        	response_body = html + "(1) a + b = " + x + "\n(2) a * b = " + y
	except ValueError:
		response_body = html + "Please enter an integer value for both a and b. OUTPUT : 1) a + b, 2) a * b"
        start_response('200 OK', [
                ('Content-Type', 'text/html'),
                ('Content-Length', str(len(response_body)))
        ])
        return [response_body]
