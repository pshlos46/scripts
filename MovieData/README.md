# MovieData
> MovieData is a short python script that fetches the list of the movies currently in Greek cinemas through TheMovieDB (themoviedb.org) API and stores them in a relational database (sqlite3). 

MovieData fetches the following information from TMDB for each movie that currently is in Greek Cinemas:

+ Title
+ Description
+ Original Title
+ Release Date
+ List of Directors
+ The IMDB link to the profile of each of the directors

## Installation - Usage

Any OS:

No installation needed. Just run ```moviedb.py``` with the correct permissions. In the first run it will create the ```movdb``` file which is the relational sqlite3 database. 
```sh
python moviedb.py
```
It has been tested with python *2.7.5/sqlite3 3.7.17* and *python 2.7.10 /sqlite3 3.20.1*. It is pretty simple and presumably will work with any python2.7/sqlite3 combination. 

## Development info

The database schema is as below. 
Tables ```movies``` and ```directors``` contain all the useful data, while ```filmdir``` is used as intermediate table to allow us to query data between the 2 tables (i.e. which movies a director has directed, or which movies have > 2 directors and their identities etc.)

```sqlite3
sqlite> .schema
CREATE TABLE movies(id INTEGER PRIMARY KEY, title TEXT, description TEXT, original_title TEXT, release_date TEXT);
CREATE TABLE directors (id INTEGER PRIMARY KEY, director TEXT, dir_url TEXT);
CREATE TABLE filmdir (film_id INTEGER, id INTEGER, PRIMARY KEY (film_id, id), FOREIGN KEY (film_id) REFERENCES movies(id), FOREIGN KEY (id) REFERENCES directors(id));
```

## Release History

* 0.4
    * First Release

## Meta

Tasos Georgiou – ageorgiou.ee@gmail.com