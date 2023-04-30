# Backend

## Install requirements

```bash
pip intall -r requirements.txt
```

## Setup Databse

```python
from app import app, db
with app.app_context():
    db.create_all()
```

## Run server locally in debug

 ```bash
 flask run
 ```

## Run server for production

```bash
gunicorn app:app
```
