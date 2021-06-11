#!/usr/bin/python3

import sys_path_helper  # Set up import paths, must be first import.

import app.settings

from upagekite import uPageKite
from upagekite.httpd import HTTPD, url
from upagekite.proto import Kite


@url("/")
def web_root(env):
    return {
        'mimetype': 'text/html',
        'body': '<h1>Hello world</h1>'}


# Configure and launch upagekite
Secrets = app.settings.Secrets()

app_env = {}
httpd = HTTPD(
    Secrets.KITE_NAME,
    app.settings.WEB_ROOT,
    app_env,
    app.settings.uPageKiteSettings)

kite = Kite(
    Secrets.KITE_NAME,
    Secrets.KITE_SECRET,
    handler=httpd.handle_http_request)

uPageKite([kite], uPK=app.settings.uPageKiteSettings).run()
