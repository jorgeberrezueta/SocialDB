from werkzeug.wrappers import Request, Response, ResponseStream

class authenticate():
    '''
    Simple WSGI middleware
    '''

    def __init__(self, app):
        self.app = app
        self.username = 'a'
        self.password = 'b'

    def __call__(self, environ, start_response):
        request = Request(environ)
        username = request.authorization['username'] or ""
        password = request.authorization['password'] or ""
        
        # these are hardcoded for demonstration
        # verify the username and password from some database or env config variable
        if username == self.userName and password == self.password:
            environ['user'] = { 'name': 'Tony' }
            return self.app(environ, start_response)

        res = Response(u'{"error": "Authorization failed"}', mimetype= 'application/json', status=401)
        return res(environ, start_response)