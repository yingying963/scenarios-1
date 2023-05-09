# Basic Docker Build

## Introduction

In this step, you will learn how to use the `docker build` command to build a basic Docker image.

## Target

The target of this step is to build a Docker image that contains a simple "Hello, World!" application.

## Result Example

Here is an example of what you should be able to accomplish at the end of this challenge:

1. Create a new directory called `hello-world` for your Docker image.

2. Create a new file called `Dockerfile` and add the following lines:

```bash
FROM alpine
RUN echo "Hello, World!"
CMD ["echo", "Hello, World!"]
```

3. Build the Docker image called `hello-world` using the `docker build` command.
