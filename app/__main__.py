from . import sys_path_helper  # Should be first
from . import settings

from upagekite.httpd import HTTPD
from upagekite import uPageKite, Kite


def main():
    secrets = settings.Secrets()
    print('=== This is `%s` configured as %s ==='
        % (settings.APP_NAME, secrets.KITE_NAME))

    if secrets.KITE_NAME and secrets.KITE_SECRET:
        shared_app_env = {}

        # Create our HTTP server object
        httpd = HTTPD(
            secrets.KITE_NAME,
            settings.WEB_ROOT,
            shared_app_env,
            settings.uPageKiteSettings)

        # Create a kite which directs traffic to the HTTP server
        kite = Kite(secrets.KITE_NAME, secrets.KITE_SECRET,
            handler=httpd.handle_http_request)

        # Launch uPageKite!
        uPageKite([kite], uPK=settings.uPageKiteSettings).run()


if __name__ == "__main__":
    main()
