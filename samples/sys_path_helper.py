import sys

SEP = '\\' if ('win' in sys.platform) else '/'
try:
    from os.path import dirname
except (ImportError, NameError):
    def dirname(fn):
        return fn.rsplit(SEP, 1)[0]


sys.path.append(SEP.join([dirname(__file__), '..']))
sys.path.append(SEP.join([dirname(__file__), '..', 'submodules', 'upagekite']))
