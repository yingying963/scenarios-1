# Building a Docker Image with Multiple Stages

## Introduction

In this step, you will learn how to use the `docker build` command to build a Docker image with multiple stages.

## Target

The target of this step is to build a Docker image that contains a Go application that is compiled in a separate stage.

## Result Example

Here is an example of what you should be able to accomplish at the end of this challenge:

1. Create a new directory called `go-app` for your Docker image.

2. Create a new file called `Dockerfile` in the `go-app` directory with the following content:

```dockerfile
FROM golang:1.14-alpine AS build
WORKDIR /app
COPY main.go .
RUN go build -o app

FROM alpine
COPY --from=build /app/app .
```

3. Create a new file called `main.go` in the `go-app` directory with the following content:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

4. Build the Docker image called `go-app` using the `docker build` command.
