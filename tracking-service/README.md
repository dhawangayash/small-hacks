# Setup the flask server
```
$ export FLASK_ENV=development
$ export FLASK_APP=track.py
```

# Run the server on local
```
$ flask run --host=127.0.0.1 --port=8080
```

# Single Line command
```
$ export FLASK_ENV=development && export FLASK_APP=track.py && flask run --host=127.0.0.1 --port=9000
```

# Usage curl command
```
curl -XPOST http://localhost:9000/api/v2/cache/ -d '{"x": "y"}'
```
