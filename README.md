# Project: Logs Analysis

This project sets up a PostgreSQL database for a news website. **Logs Analysis** is a command line tool that  will use information from the database to discover what kind of articles the site's readers like.


The provided Python script [main.py](src/main.py) uses the psycopg2 library to query the database
and produce a report that answers the following questions:
* What are the most popular three articles of all time?
* Who are the most popular article authors of all time?
* On which days did more than 1% of requests lead to errors?

# Setup

* Install [VirtulBox](https://www.virtualbox.org/wiki/Downloads)
* Install [Vagrant](https://www.vagrantup.com/downloads.html)
* Download [VM File](https://github.com/udacity/fullstack-nanodegree-vm) (VM includes Python 2.7.12, PostgreSQL), then to setup VM:
    ```
    cd /vagrant
    vagrant up
    vagrant ssh
    ```
* Import _news_ database to PostgreSQL
    * Download [database script](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)
    * Unzip it and run:
    `psql -d news -f newsdata.sql` to import data to _news_ database

# Database
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. 

_News_ database consists from three tables:
* _articles_ table:
```
                                 Table "public.articles"
 Column |           Type           |                       Modifiers
--------+--------------------------+-------------------------------------------------------
 author | integer                  | not null
 title  | text                     | not null
 slug   | text                     | not null
 lead   | text                     |
 body   | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('articles_id_seq'::regclass)
Indexes:
    "articles_pkey" PRIMARY KEY, btree (id)
    "articles_slug_key" UNIQUE CONSTRAINT, btree (slug)
Foreign-key constraints:
    "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
```
* _authors_ table:
```
                         Table "public.authors"
 Column |  Type   |                      Modifiers
--------+---------+------------------------------------------------------
 name   | text    | not null
 bio    | text    |
 id     | integer | not null default nextval('authors_id_seq'::regclass)
Indexes:
    "authors_pkey" PRIMARY KEY, btree (id)
Referenced by:
    TABLE "articles" CONSTRAINT "articles_author_fkey" FOREIGN KEY (author) REFERENCES authors(id)
```
* _log_ table:
```
                                  Table "public.log"
 Column |           Type           |                    Modifiers
--------+--------------------------+--------------------------------------------------
 path   | text                     |
 ip     | inet                     |
 method | text                     |
 status | text                     |
 time   | timestamp with time zone | default now()
 id     | integer                  | not null default nextval('log_id_seq'::regclass)
Indexes:
    "log_pkey" PRIMARY KEY, btree (id)
```


# Run
```
 pip install -r requirements.txt
 python src/main.py
```
# Usage

Use question numbers to get answers or anything else to exit application.

### Example output:

```
This application can give you an answer to following question:
1: What are the most popular three articles of all time?
2: Who are the most popular article authors of all time?
3: On which days did more than 1% of requests lead to errors?

Put the question number or anything else to exit application.
Enter question number:1

Answer:
"Candidate is jerk, alleges rival" - 338647 views
"Bears love berries, alleges bear" - 253801 views
"Bad things gone, say good people" - 170098 views
```