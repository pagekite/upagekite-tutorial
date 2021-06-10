# upagekite - Tutorial and Template

## Introduction

This is a tutorial and application template for people getting started
building webapps using [upagekite][1] the MicroPython/ESP32 *public
facing* web framework.

The main difference between [upagekite][1] and other Python web
frameworks are:

   1. [upagekite][1] is small, simple and self containd - intended for
      modest hardware (like the ESP32) and low-traffic, simple web-apps.
   2. [upagekite][1] makes it very easy to expose your webapp to the
      public Internet so you can interact with it from anywhere. You can
      also use upagekite to build local apps (including captive portals),
      but it assumes the goal is to go public and make your device part
      of the World Wide Web.

The latter is accomplished using the [PageKite][2] relay protocol, and
by default [upagekite][1] assumes you are using the [pagekite.net][2]
public relays. Note this is a paid service, but the trial is free and
there are zero-cost options available for people of limited means. If
you prefer to DIY, the [relay itself][3] is also fully open source.


## Prerequisites

   1. Sign up for an account at <https://pagekite.net/>
   2. Install **micropython** or **Python 3.8+**

Optionally, if you are targetting the ESP32, install [a recent (1.14+)
version of MicroPython](https://micropython.org/download/) on your device.


## Getting Started

    # 1. Fork this repository on github?
    ...

    # 2. Clone the reposity for local work
    #    Replace the URL with yoru fork, if you prefer.
    #
    git clone https://github.com/upagekite/upagekite-tutorial

    # 3. Initialize and update the `upagekite` submodule
    git submodule init
    git submodule update

    # 4. Add your pagekite.net credentials to `private/settings.py`
    ...

    # 5. Run `hello.py` to verify it works!
    python3 samples/hello.py
    micropython samples/hello.py

NOTE: this project template configures `git` to ignore changes made
under `private/` - you will not be prompted to commit those changes.
This is to avoid accidentally leaking credentials to Github or other
code sharing sites.


## Choose your Adventure!

You are now ready to proceed to one of the available tutorials





[1]: https://github.com/pagekite/upagekite
[2]: https://pagekite.net/
[3]: https://github.com/pagekite/PyPagekite
