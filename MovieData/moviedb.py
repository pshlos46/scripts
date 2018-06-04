# MovieData v0.4
# 5-10-2017

import json
import requests
import sqlite3

# global constants
DB_NAME = 'movdb'
TOKEN = '<insert your themoviedb API token>'


def create_db(db_name):
    # Create an SQLite3 DB and our tables for our project
    try:
        db = sqlite3.connect(db_name)
        cursor = db.cursor()
        # Check if tables movies, directors and intermediate table filmdir does not exist and create them
        cursor.execute('''CREATE TABLE IF NOT EXISTS movies(id INTEGER PRIMARY KEY, title TEXT, description TEXT, original_title TEXT, release_date TEXT);''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS directors (id INTEGER PRIMARY KEY, director TEXT, dir_url TEXT);''')
        cursor.execute('''CREATE TABLE IF NOT EXISTS filmdir (film_id INTEGER, id INTEGER, PRIMARY KEY (film_id, id), FOREIGN KEY (film_id) REFERENCES movies(id), FOREIGN KEY (id) REFERENCES directors(id));''')
        db.commit()
    except Exception as e:
        db.rollback()
        raise e
    finally:
        db.close()


def create_connection(db_file):
    # use it to create connection to DB
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Exception as e:
        print(e)


def insert_DB(conn, table, d):
    # function to handle inserting to DB tables - input a dictionary of the results d and the table to insert
    # The dual queries work as  "INSERT ... ON DUPLICATE KEY UPDATE" statement in MySQL. sqlite does not support that
    # statement so we had to work around it
    sql = 'INSERT OR IGNORE INTO '+table+' ({}'.format(','.join('{}'.format(k) for k in d))+') VALUES({}'.format(','.join('?'.format(v) for v in d.itervalues()))+');'
    sql2 = 'UPDATE '+table+' SET {}'.format(', '.join('{}=?'.format(k) for k in d if k != 'id'))+' WHERE changes()=0 AND id=?;'

    cur = conn.cursor()
    cur.execute(sql, d.values())
    cur.execute(sql2, d.values())
    conn.commit()


def apicall(kind, f):
    # function to handle the apicalls - input the kind of apicall we need (now playing, credits, person details etc.)
    # and f is used to provide different things according to the apicall (i.e. page, id etc.)
    start = 'https://api.themoviedb.org/3/'
    urlind = {'np': '%smovie/now_playing?api_key=%s&page=%s&region=GR' % (start, TOKEN, f),
              'cred': '%smovie/%s/credits?api_key=%s' % (start, f, TOKEN),
              'dr': '%sperson/%s?api_key=%s&language=en-US' % (start, f, TOKEN)}
    url = urlind[kind]
    response = requests.get(url)
    return json.loads(response.text)


def main():

    # create a DB if it doesn't exist
    create_db(DB_NAME)
    # create a database connection
    conn = create_connection(DB_NAME)

    # Use i and while...True to get all the pages from the TMDB api as it needs to manual cycle through them
    i = 1
    while True:
        np_json = apicall('np', i)
        # traverse results list from output json and store movie/credits/person values and call the relevant jsons needed
        # subsequently to crawl the data we need
        for elem in np_json['results']:
            cred_json = apicall('cred', elem['id'])
            # update our movies table
            insert_DB(conn, 'movies', {'id': elem['id'], 'title': elem['title'], 'description': elem['overview'], 'original_title': elem['original_title'], 'release_date': elem['release_date']})
            for item in cred_json['crew']:
                if item['job'] == 'Director':
                    dr_json = apicall('dr', item['id'])
                    # update our directors table and filmdir intermediate table
                    insert_DB(conn, 'directors', {'id': item['id'], 'director': item['name'], 'dir_url': ("www.imdb.com/name/%s" % (dr_json['imdb_id']))})
                    insert_DB(conn, 'filmdir', {'film_id': elem['id'], 'id': item['id']})
        i += 1
        if i > np_json['total_pages']:
            break

    # Close connection to DB after the script finishes
    conn.close()

if __name__ == '__main__':
    main()
