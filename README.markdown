Safe Templates
==============

An exploration into using [Jinja2](http://jinja.pocoo.org) for user-modifiable, safe templating.

The present goal is to have a fixed location on the server, into which the user can upload Templates 
and/or store templates in a database table and use them to render data from a known API.

I have chosen [Flask](http://flask.pocoo.org) to develop this solution.

Jinja provides a [sandboxed environment](http://jinja.pocoo.org/2/documentation/sandbox) to evaluate 
untrusted code. 
