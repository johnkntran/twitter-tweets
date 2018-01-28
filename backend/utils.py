"""
Utility class to help with sending and receiving web requests and responses.

This file goes where your backend scripts are being served, such as 
/Library/WebServer/CGI-Executables on a Mac, or /var/www/wsgi-scripts on CentOS.
"""

import config
import webob

class util(object):
	"""
	Utility class that helps with managing HTTP requests and responses. The 
	`environ` and `start_response` objects comes from the WSGI message from the 
	application.
	"""

	def __init__(self, environ, start_response):
		"""
		Initialize a `util` instance to help with managing HTTP 
		requests/responses.
		"""
		self.environ = environ
		self.start_response = start_response

	def get_cookie(self):
		"""
		Retrieve the session cookie from the HTTP request if one exists.
		"""
		req = webob.Request(self.environ)
		return req.cookies.get('session')

	def send_data(self, output, sess_id=None):
		"""
		Send data out as an HTTP Response object using the `environ` received 
		from the WSGI.
		"""
		resp = webob.Response(body=output, content_type='application/json')
		resp.content_length = len(output)
		resp.cache_control = 'private, no-cache, no-store'
		resp.headers['X-Frame-Options'] = 'SAMEORIGIN'
		resp.headers['Access-Control-Allow-Origin'] = '*'
		resp.headers['Access-Control-Allow-Headers'] = 'origin, content-type, accept'
		if sess_id:
			resp.set_cookie(name='session', value=sess_id, expires=None, 
				secure=config.USE_HTTPS, httponly=True, overwrite=True)
		return resp(self.environ, self.start_response)
