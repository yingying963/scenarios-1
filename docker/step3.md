# Building a Docker Image with Environment Variables

## Introduction

In this step, you will learn how to use the `docker build` command to build a Docker image that includes environment variables.

## Target

The target of this step is to build a Docker image that contains a Python application that uses an environment variable to set the port number.

## Result Example

Here is an example of what you should be able to accomplish at the end of this challenge:

1. Create a new directory `flask-app-env` for your Docker image.

2. Create a new file called `Dockerfile` add the following lines:

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
COPY app.py .
RUN pip install -r requirements.txt
ENV PORT=5000
```

3. Create a new file called `app.py` in the `flask-app-env` directory with the following content:

```python
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('PORT'))
```

4. Build the Docker image called `flask-app-env` using the `docker build` command.
