# VeSafe Transaction API

*Description*
===========
This is Transaction API for VeSafe Interface


Requirements
============
See [requirements.txt](./requirements.txt).

Run:
```commandline
  git clone git@gitlab.rinznetwork.com:scan-hub/sh-lib.git lib
  pip install -f ./lib/requirements.txt
  pip --no-cache-dir install "Flask[async]"

```
Usage
=====
Run the following commands start the server (assumes activated Python3 virtual env):

Run:
```python main.py```



Request
=====

- URL: ```/{veriosn}/{service}/{model}/{action}```

- Response:
```
    {
         "data": object,
         "error_code": string,
         "errors": object,
         "msg": string
    }
```
- Status code:
```
    200: OK
    400: Bad request
    402: Payment Required
    403: Forbidden
    404: NotFound
    405: Method Not Allowed
    500: Internal Server Error
```
- Error: exception.py
```commandline

class BadRequest(Exception):
    def __init__(self, *args: object) -> None:
        super().__init__(*args)
        self.status_code = 404
        self.msg = '....'
        self.errors = []
        self.error_code = 'E_BAD_REQUEST'

    pass

# Use:

def endpoint():
 ....
 
 raise BadRequest

```
Security:
====

- Authentication:
    + Type: Bearer [token]
    + Token: base64 encode
    + Data:
    ````
    {
        "payload": "{info}",
        "signature": "signature of auth service"
    }

Worker:
===

- For write db:
  ```commandline
    # init model with broker at models/__init__.py
     
    __models__ = ['modelName']
 
    modelName = TestDao(connect_db.db.test, broker=Config.BROKER_URL, project=Config.PROJECT)
     
    # worker
      modelName.insert_one(..., worker=True) # return draft
      modelName.update_one(..., worker=True) # return None
    # No worker
      modelName.insert_one({..}) # return raw
  ```
- Worker for write db:
  ```commandline
     celery --app worker worker -Q <db_name>-<PROJECT_NAME>-queue -l INFO -c 4
  ```


Project structure:
====

```
    ├── README.rst
    ├── main.py
    ├── models
    │   ├── __init__.py
    │   ├── dao.py
    ├── helper
    │   ├── __init__.py
    ├── tasks
    │   ├── __init__.py
    │   ├── task_name.py
    ├── resources
    │   ├── __init__.py
    │   ├── todo.py
    │       ├── def get
    │       └── def post
    ├── worker.py
    ├── util.py
    ├── security.py
    ├── requirements.txt
    └── config.py
```

* resources - holds all endpoints.
* main.py - flask application initialization.
* config.py - all global app config.