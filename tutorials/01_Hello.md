# uPageKite Tutorial: Hello World

**Topics:**
 *serving static files*,
 *configuring upagekite*,
 *starting upagekite*

**Prerequisites:**
 [Install upagekite](../README.md),
 [Register a pagekite.net account](https://pagekite.net/signup/)

-----------------------------------------------------------------------------

Once you have completed the prerequisites, building a public-facing uPageKite
web server can be done in only a few lines of code.


## 1. Prepare your app settings

All uPageKite apps need a "kite name", which is the public domain name for
the exposed website. Websites are exposed to the Internet using a PageKite
relay, and the relays require authentication - a kite secret.

Simple apps can configure these as static variables in code, more complex
ones will want to load these settings from a configuration file (the app
template places these in `private/secrets.json`).

For the purpose of this tutorial, we create a few simple constants which
will used later on:

    KITE_NAME = 'YOURKITE.pagekite.me'
    KITE_SECRET = 'YOUR SECRET'

You will also need a "web root", a directory containing the static content
(CSS files, Javascript, etc.) of your website. This tutorial ships with a
static folder containing an `index.html` and `robots.txt`, which you could
use like so:

    WEB_ROOT = '/path/to/tutorial/static'

Most apps will also have settings and their own internal logic which needs
to be accessible at various points. To facilitate this, we create a default
"request environment", named `req_env`:

    req_env = {'something': "Custom app data goes here"}


## 2. Configure uPageKite

Configuring the uPageKite relay system is done by subclassing
`pagekite.proto.uPageKiteDefaults` and changing a few constants.

The defaults are fine for connecting to the
[pagekite.net](https://pagekite.net/) public relays, but especially during
development, you will probably want to enable more verbose logging, like so:

    from upagekite.proto import uPageKiteDefaults

    ...

    class myPageKiteSettings(uPageKiteDefaults):
        info = uPageKiteDefaults.log
        debug = uPageKiteDefaults.log
        error = uPageKiteDefaults.log

This class will then be passed to the PageKite web server and manager objects
when they are created.


## 3. Create and configure your HTTP server

uPageKite comes with its own built-in HTTP server, which can serve static
files, run single-shot "CGI-like" python scripts or invoke pre-registered
handlers like most modern web frameworks.

    from upagekite.httpd import HTTPD

    ...

    httpd = HTTPD(KITE_NAME, WEB_ROOT, shared_req_env, myPageKiteSettings)


## 4. Create a kite

A "kite" defines the link between your service's public identity (DNS name,
protocol, port number) and the actual code which handles incoming requests.

In this case, we link the `KITE_NAME` to the HTTP server's default request
handler:

    from upagekite.proto import Kite

    ...

    kite = Kite(KITE_NAME, KITE_SECRET, handler=httpd.handle_http_request)


## 5. Launch uPageKite!

Finally we create a `uPageKite` controller object, which takes care of
connecting to the relays and passing requests back and forth between the
HTTP server and the PageKite tunnel:

    from upagekite import uPageKite

    ...

    pk_control = uPageKite([kite], uPK=myPageKiteSettings)

    # Run until aborted by CTRL+C
    pk_control.run()


## 6. Putting it all together

Assembling the above fragments into a single Python script, we end up with
something that looks a bit like this:

    from upagekite import uPageKite
    from upagekite.proto import uPageKiteDefaults, Kite
    from upagekite.httpd import HTTPD


    KITE_NAME = 'YOURKITE.pagekite.me'
    KITE_SECRET = 'YOUR SECRET'

    WEB_ROOT = '/path/to/tutorial/static'


    class myPageKiteSettings(uPageKiteDefaults):
        info = uPageKiteDefaults.log
        debug = uPageKiteDefaults.log
        error = uPageKiteDefaults.log


    req_env = {'something': "Custom app data goes here"}

    httpd = HTTPD(KITE_NAME, WEB_ROOT, shared_req_env, myPageKiteSettings)

    kite = Kite(KITE_NAME, KITE_SECRET, handler=httpd.handle_http_request)

    pk_control = uPageKite([kite], uPK=myPageKiteSettings)

    pk_control.run()


You should be able to copy/paste this into file named `hello.py`, edit
to your liking and then run it using the Python 3 interpretor. That
might look something like this:

    tutorial$ python3 hello.py
    [162..490] Tick: uPageKite 0.0.1u; back_off=1; relays=0; socks=0
    [162..375] Ping ('185.112.146.199', 443) ok: 25ms (~22ms)
    ...
    [162..382] Ping ('139.162.5.63', 443) ok: 543ms (~543ms)
    [162..716] Flying http://YOURKITE.pagekite.me via ('185.112.146.199', 443)
    [162..006] Connected to ('185.112.146.199', 443)
    [162..695] DNS update YOURKITE.pagekite.me to 185.112.146.199: ...

Once the DNS update is complete, you should be able to load
`https://YOURKITE.pagekite.me/` in a browser and see the contents of
`static/index.html`: Hello Static World!

-----------------------------------------------------------------------------
