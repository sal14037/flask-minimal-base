# Basic Flask App

## Description
A minimal starter for a Flask API, includes auto generated openapi documentation out of the box.

Features:
* rest-x
* flask_sqlalchemy
* flask_migrate

## Run

Start the server

```bash
$ python manage.py run
```

Access the [OpenAPI](127.0.0.1:5000/v1/) doc.

## (optional) SQLite database

Create .env file and add the following lines

```
DB_URL="sqlite:///../data.db"
```

Start create_db() in terminal

```bash
$ python manage.py create_db
```

Now you should see the data.db file in your working tree.

#### Done! 
Pretty fly for a Flask API! Now you can head back to your OpenAPI doc and try it out. 