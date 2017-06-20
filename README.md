[![Build Status](https://travis-ci.org/giving-a-fuck-about-climate-change/carbondoomsday.svg?branch=master)](https://travis-ci.org/giving-a-fuck-about-climate-change/carbondoomsday)

# carbondoomsday

A Django web app that gives a fuck.

Work. In. Progress.

# Current Misson

From [this discussion]:

[this discussion]: https://github.com/giving-a-fuck-about-climate-change/carbon-doomsday/issues/5#issuecomment-307584468:

> Let's get the coinbase-inspired CO2 MVP prototyped and launched, get
> eyeballs, collaborators, and media and keep our eyes peeled on what emerges
> from there.

# Mega Unstable Docker Development Setup

You'll need to have Docker installed. The following `devdocker` script command
will run a dockerized postgresql instance and a development only version of the
django app that serves the scraped data ([source]) for use in writing a
front-end client.

[source]: https://www.esrl.noaa.gov/gmd/webdata/ccgg/trends/co2_mlo_weekly.csv

``` bash
$ git clone git@github.com:giving-a-fuck-about-climate-change/carbondoomsday.git
$ cd carbondoomsday
$ ./bin/devdocker up
```

You can then hit [http://127.0.0.1:8089/](http://127.0.0.1:8089/) for the
Swagger documentation. You can browse the data and use the filters in the
browsable API explorer to get familiar with the end-point. That should be
enough for now to start writing a front-end that consumes data.

When you're finished, just run:

```
$ ./bin/devdocker down
```

I'm hacking away on various things, so please complain at [the lobby] if it breaks.

[the lobby]: https://gitter.im/giving-a-fuck-about-climate-change/Lobby
