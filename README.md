# rando
generate random numbers into a stream, send them
over a NSQ `topic`, then have workers listen on
specific `channels` to calculate stuff like:

* is the given number prime?
* is the given number odd?
* is the given number greater than 100?
