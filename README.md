# rdbms-partition-tests

## Setup & Usage

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ mkdir data
(venv) $ docker compose up -d postgresdb
(venv) $ python setup.py drop # drop the database
(venv) $ python setup.py init  # init the database
(venv) $ python setup.py populate   # populate rows
(venv) $ python setup.py drop # drop the database
```

## Selecting MySQL or Postgres

In the setup.py file, change the DB string pointed to be DATABASE_STRING
```python
MYSQL_CONNECTION_STRING = "mysql://root:rootpassword@0.0.0.0:3306/tsp"
POSTGRES_CONNECTION_STRING = "postgresql://postgres:password@0.0.0.0:5432/tsp"

DATABASE_STRING = POSTGRES_CONNECTION_STRING
```