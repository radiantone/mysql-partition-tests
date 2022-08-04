# mysql-partition-tests

## Setup & Usage

```bash
$ python3 -m venv venv
$ source venv/bin/activate
(venv) $ pip install -r requirements.txt
(venv) $ docker compose up -d
(venv) $ python setup.py init  # init the database
(venv) $ python setup.py populate   # populate rows
(venv) $ python setup.py drop # drop the database
```