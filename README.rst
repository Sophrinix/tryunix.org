tryunix.org - Try Unix (in a browser)
=====================================

.. Note:: This is a tribute to the over-eagerness,
   confidence, eerie clarity of mind provided by the early
   onset of ADHD Meds. I wish I was joking. Combine this
   with hyperfocus and you get a night well spent writing
   code you can't even wrap your head around the next day.

About
-----

This is a rather sad attempt at recreating something like
tryruby.org, tryerlang.org, tryhaskell.org and the likes.

I thought something completely stupid like:

  "Hey! I love Unix and wish to get people to try it! I also know some Python! 
  And I know for a *fact* that jquery-console_ exists! And I basically know how RESTful
  web services work, and could probably get away with writing a simple backend to such a console
  that could emulate a basic unix system! **How hard can it be?**

And then the Adderall wore off and I found myself biting my lower lip, looking at the receipt for the purchase of the tryunix.org_ domain, and the very scarce documentation_ for WebCore_ (however the code_ is very, very readable, so that's not insurmountable). Still, I sat there with a single sentence resonating through my thoughts, as read by some aggravated deity's booming voice:

  *OH GOD WHAT HAVE YOU DONE?*

Hopefully one day, this code will be functional and I can say I'm the creative mastermind behind the piece of crud that is tryunix.org_.

Requirements
-------------

So far not only is project not even close to functional, but I am pedant enough to list
the requirements as they come.

System:
~~~~~~~~
 * Python 2.5+
 * virtualenv_ is strongly recommended
 * distribute/setuptools (should be pretty standard)
 * A decent web server supporting WSGI

              -- OR --

 * gunicorn_ behind something like nginx_.

Python Modules:
~~~~~~~~~~~~~~~~  
 * WebCore_
 * Genshi_
 * Beaker_

Very Quick Hacker's Guide to Poking at the Source
---------------------------------------------------

 1. ``$ mkdir ~/.python-envs/``
 2. ``$ virtualenv --distribute --no-site-packages ~/.python-envs/tryunix``
 3. ``$ source ~/.python-envs/tryunix/bin/activate``
 4. ``(tryunix)$ pip install WebCore``
 5. ``(tryunix)$ git clone https://github.com/mrdaemon/tryunix.org.git``
 6. ``(tryunix)$ cd tryunix.org && python setup.py develop``

You're set. Run `paster serve --reload dev.ini` to launch the app,
the point your browser at http://127.0.0.1:8888/

It should work. At some point. Eventually. But you'll probably staring at broken code
and the nastiest tracebacks known to man.

Feel free to fork and contribute once there's some meat there.

.. _jquery-console: https://github.com/chrisdone/jquery-console
.. _tryunix.org: http://tryunix.org

.. _virtualenv: http://pypi.python.org/pypi/virtualenv
.. _gunicorn: http://gunicorn.org/
.. _nginx: http://nginx.org/

.. _Genshi: http://genshi.edgewall.org/
.. _Beaker: http://pypi.python.org/pypi/Beaker/0.7.3

.. _WebCore: http://web-core.org/
.. _documentation: http://packages.python.org/WebCore/
.. _code: https://github.com/GothAlice/WebCore