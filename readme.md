# Python RESTful API using Flask & SQLAlchemy & Marshmallow + Unit Tests

> Create, read, update and delete objects from a SQLite DB via a RESTful API written in Python, using Flask, SQLite, SQLAlchemy & Marshmallow, including unit tests

## Quick Start

``` bash
# Install dependencies
$ pip install -r requirements.txt

# Create DB
$ python
>> from app import db
>> db.create_all()
>> exit()

# Run Server (http://localhost:8080)
flask run
```

## Endpoints

* GET     /product
* GET     /product/:id
* POST    /product
* PUT     /product/:id
* DELETE  /product
* DELETE  /product/:id

## Unit Tests

``` bash
# To run only the tests
python -m unittest discover __unittests__

# To get a coverage report
coverage run -m unittest discover __unittests__/
coverage report -m
```
