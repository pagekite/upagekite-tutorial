##############################################################################
# Note: The author has placed this work in the Public Domain, thereby        #
#       relinquishing all copyrights.  Everyone is free to use, modify,      #
# republish, sell or give away this work without prior consent from anybody. #
##############################################################################

from . import sys_path_helper  # Should be first
from . import settings
from . import web

from upagekite.httpd import HTTPD
from upagekite import uPageKite, Kite


def main():
    secrets = settings.Secrets()
    print('=== This is `%s` configured as %s ==='
        % (settings.APP_NAME, secrets.KITE_NAME))

    if secrets.KITE_NAME and secrets.KITE_SECRET:
        # These things are added to the req_env dict passed to any dynamic
        # URL handlers, and the global environment when running .py files
        # from within the webroot.
        shared_req_env = {
            'something': 'Hello Templated World!'}

        # Create our HTTP server object
        httpd = HTTPD(
            secrets.KITE_NAME,
            settings.WEB_ROOT,
            shared_req_env,
            settings.uPageKiteSettings)

        # Create a kite which directs traffic to the HTTP server
        kite = Kite(secrets.KITE_NAME, secrets.KITE_SECRET,
            handler=httpd.handle_http_request)

        # Launch uPageKite!
        uPageKite([kite], uPK=settings.uPageKiteSettings).run()


if __name__ == "__main__":
    main()
