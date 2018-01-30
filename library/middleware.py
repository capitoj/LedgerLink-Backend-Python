

class LibraryMiddleware(object):

    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response


def load_app_assets_in_context(request):
    return {'library_js': ('jsfile1.js', 'jsfile2.js',), 'library_css': 'csfile1.css'}
