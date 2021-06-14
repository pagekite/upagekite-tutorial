##############################################################################
# Note: The author has placed this work in the Public Domain, thereby        #
#       relinquishing all copyrights.  Everyone is free to use, modify,      #
# republish, sell or give away this work without prior consent from anybody. #
##############################################################################
#
# This is a common place for app settings
#
from .sys_path_helper import app_root, path_join
from upagekite.proto import uPageKiteDefaults

APP_NAME = "uPageKite Tutorial App"
PATH_SECRETS = path_join('private', 'secrets.json')
WEB_ROOT = 'static'


class uPageKiteSettings(uPageKiteDefaults):
    """
    This is a configuration object for uPageKite.

    Mostly we inherit the defaults.
    """
    # Enable basic logging (uncomment debug or trace for more)
    info = uPageKiteDefaults.log
    error = uPageKiteDefaults.log
    debug = uPageKiteDefaults.log
    #trace = uPageKiteDefaults.log


class Secrets:
    """
    These are private settings which get loaded from private/secrets.json
    """
    KITE_NAME   = property(lambda self: self.secrets.get('kite_name'))
    KITE_SECRET = property(lambda self: self.secrets.get('kite_secret'))

    def __init__(self):
        import sys, json
        try:
            self.secrets = json.load(open(PATH_SECRETS, 'r'))
        except Exception as e:
            sys.stderr.write('WARNING: Failed to load settings from %s: %s\n'
                % (PATH_SECRETS, e))
            self.secrets = {}
