# Solution

1. Create a new directory for your Docker image:

```bash
mkdir go-app
cd go-app
```

2. Create a new file called `Dockerfile` in the `go-app` directory:

```bash
touch Dockerfile
```

3. Open the `Dockerfile` in a text editor and add the following lines:

```dockerfile
FROM golang:1.14-alpine AS build
WORKDIR /app
COPY main.go .
RUN go build -o app

FROM alpine
COPY --from=build /app/app .
```

4. Save and close the `Dockerfile`.

5. Create a new file called `main.go` in the `go-app` directory:

```bash
touch main.go
```

6. Open the `main.go` file in a text editor and add the following lines:

```go
package main

import "fmt"

func main() {
    fmt.Println("Hello, World!")
}
```

7. Save and close the `main.go` file.

8. Build the Docker image using the `docker build` command:

```bash
docker build -t go-app .
```
