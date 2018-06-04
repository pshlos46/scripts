CREATE TABLE movies(id INTEGER PRIMARY KEY, title TEXT, description TEXT, original_title TEXT, release_date TEXT);
CREATE TABLE directors (id INTEGER PRIMARY KEY, director TEXT, dir_url TEXT);
CREATE TABLE filmdir (film_id INTEGER, id INTEGER, PRIMARY KEY (film_id, id), FOREIGN KEY (film_id) REFERENCES movies(id), FOREIGN KEY (id) REFERENCES directors(id));
