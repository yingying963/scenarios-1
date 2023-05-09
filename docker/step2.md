# Building a Docker Image with Dependencies

## Introduction

In this step, you will learn how to use the `docker build` command to build a Docker image that includes dependencies.

## Target

The target of this step is to build a Docker image that contains a Python application that requires the Flask library.

## Result Example

Here is an example of what you should be able to accomplish at the end of this challenge:

1. Create a new directory called `flask-app` for your Docker image.

2. Create a new file called `Dockerfile` add the following lines:

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
```

3. Create a new file called `requirements.txt` and add the following line:

```bash
Flask==1.1.2
```

4. Build the Docker image called `flask-app` using the `docker build` command.
