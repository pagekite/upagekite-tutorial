##############################################################################
# Note: The author has placed this work in the Public Domain, thereby        #
#       relinquishing all copyrights.  Everyone is free to use, modify,      #
# republish, sell or give away this work without prior consent from anybody. #
##############################################################################

from upagekite.httpd import url


@url('/hello/dynamic')
def web_hello_dynamic(req_env):
    yield {
        'mimetype': 'text/html; charset="UTF-8"',  # This is the default
        'suppress_log': True,     # Avoid logging this request twice
        'ttl': 30}                # Expire quickly from the browser cache!

    print('Calculating some things, this never runs on HTTP HEAD')
    remote_ip = req_env.remote_ip
    user_agent = req_env.http_headers.get('User-Agent', 'Unknown Browser')
    something = req_env['something']
    yield (
        '<h1>Hello %s at %s! Hér er smá íslenska!</h1>\n'
        '<p>Our something is: %s</p>\n'
        '<p>Our query_vars are: %s</p>\n'
        ) % (user_agent, remote_ip, something, req_env.query_vars)

