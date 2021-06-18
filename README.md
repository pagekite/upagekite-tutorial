# upagekite - Tutorial and App Template


**WARNING:** This is a work in progress! It's nowhere near complete.


## Introduction

This is a tutorial and application template for people getting started
building webapps using [upagekite][1], the MicroPython/ESP32-friendly
*public facing* web framework.

The main difference between [upagekite][1] and other Python web
frameworks are:

   1. [upagekite][1] is small, simple and self contained - intended for
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

It is possible to run a working, dynamic website using [upagekite][1]
and MicroPython in only a few hundred kilobytes of RAM; the library was
tested and developed using the ESP32 DevKitC, which only has 520kB of
RAM!


## Prerequisites

   1. Sign up for an account at <https://pagekite.net/signup/>
   2. Install **micropython** or a recent **Python 3.x**

Optionally, if you are targetting the ESP32, install [a recent (1.14+)
version of MicroPython](https://micropython.org/download/) on your device.

For MicroPython (or Pycopy) on Unix, you may also need:

   * micropython -m upip install pycopy-uasyncio


## Getting Started

    # 1. Fork this repository on github?  (optional)
    ...

    # 2. Clone the reposity for local work.
    #    Replace the URL with your fork, if you created one.
    #
    git clone https://github.com/upagekite/upagekite-tutorial

    # 3. Initialize and update the `upagekite` submodule
    git submodule init
    git submodule update

    # 4. Add your pagekite.net credentials to `private/secrets.json`
    cp private/secrets.json.sample private/secrets.json
    nano private/secrets.json

    # 5a. Run the template app to verify it works!
    python3 -m app

    # 5b. Or, run the template app using MicroPython:
    micropython -m app

    # 6. In another terminal, try to fetch `/robots.txt`
    curl https://YOURKITE.pagekite.me/robots.txt


NOTE: this project template configures `git` to ignore changes made
under `private/` - you will not be prompted to commit those changes.
This is to avoid accidentally leaking credentials to Github or other
code sharing sites.


## Choose Your Adventure!

You are now ready to proceed to one of the available tutorials:

   * [Hello World](tutorials/01_Hello_World.md) (standalone)

The following tutorials all assume you are using the provided app
template:

   * [Dynamic Hello World](tutorials/02_Dynamic_Hello_World.md)



## Copyright and Credits

This tutorial is (C) Copyright 2021, Bjarni R. Einarsson and [The
Beanstalks Project ehf][3].

The author has placed some included Python code samples in the Public
Domain, thereby relinquishing all copyrights. Everyone is free to use,
modify, republish, sell or give away the samples without prior consent
from anybody. The samples this applies to, contain comments which make
this clear on a file-by-file bases.


[1]: https://github.com/pagekite/upagekite
[2]: https://pagekite.net/
[3]: https://github.com/pagekite/PyPagekite
[3]: https://pagekite.net/company/
