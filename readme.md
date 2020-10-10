# Python RESTful API using Flask & SQLAlchemy & Marshmallow

> Create, read, update and delete objects from a SQLite DB via a RESTful API written in Python, using Flask, SQLite, SQLAlchemy & Marshmallow

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