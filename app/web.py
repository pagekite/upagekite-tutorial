##############################################################################
# Note: The author has placed this work in the Public Domain, thereby        #
#       relinquishing all copyrights.  Everyone is free to use, modify,      #
# republish, sell or give away this work without prior consent from anybody. #
##############################################################################

from upagekite.httpd import url


@url('/hello/dynamic')
def web_hello_dynamic(req_env):
    remote_ip = req_env.remote_ip
    user_agent = req_env.http_headers.get('User-Agent', 'Unknown Browser')
    something = req_env['something']

    body = (
        '<h1>Hello %s at %s!</h1>\n'
        '<p>Our something is: %s</p>\n'
        ) % (user_agent, remote_ip, something)

    return {
        'body': body,
        'mimetype': 'text/html',  # This is actually the default
        'ttl': 30}                # Expire quickly from the browser cache!

