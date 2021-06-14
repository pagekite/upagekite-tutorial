#!/usr/bin/python3
##############################################################################
# Note: The author has placed this work in the Public Domain, thereby        #
#       relinquishing all copyrights.  Everyone is free to use, modify,      #
# republish, sell or give away this work without prior consent from anybody. #
##############################################################################
#
# This is a minimal, single-file uPageKite "hello world" web server.
#
# It should provide responses on the following URL paths:
#
#    /
#    /hello/dynamic
#    /robots.txt
#
# You will need to edit KITE_NAME and KITE_SECRET to get it to work.
#
from sys_path_helper import path_join, app_root

from upagekite import uPageKite
from upagekite.httpd import HTTPD, url
from upagekite.proto import Kite, uPageKiteDefaults


KITE_NAME = 'YOURKITE.pagekite.me'
KITE_SECRET = 'YOUR SECRET'

WEB_ROOT = path_join(app_root(), 'static')  # Contains index.html & robots.txt


# This class configures uPageKite for your app; by default it uses the
# pagekite.net public relays and logs very little.
class myPageKiteSettings(uPageKiteDefaults):
    info = uPageKiteDefaults.log
    debug = uPageKiteDefaults.log


# Register a simple handler for our dynamic hello page
@url('/hello/dynamic')
def web_hello_dynamic(req_env):
    remote_ip = req_env.remote_ip
    user_agent = req_env.http_headers.get('User-Agent', 'Unknown Browser')

    something = req_env['something']  # Custom data added by our app.

    body = (
        '<h1>Hello %s at %s!</h1>\n'
        '<p>Our something is: %s</p>\n'
        ) % (user_agent, remote_ip, something)

    return {
        'body': body,
        'mimetype': 'text/html',  # This is actually the default
        'ttl': 30}                # Expire quickly from the browser cache!


# These things are added to the req_env dict passed to any dynamic URL
# handlers, and the global environment when running .py files from
# within the webroot.
shared_req_env = {'something': 'An Example'}

# Create our HTTP server
httpd = HTTPD(KITE_NAME, WEB_ROOT, shared_req_env, myPageKiteSettings)

# Create our kite, directing any requests to the HTTP server
kite = Kite(KITE_NAME, KITE_SECRET, handler=httpd.handle_http_request)

# Fly the kite, serve forever...
pk_control = uPageKite([kite], uPK=myPageKiteSettings)
pk_control.run()
