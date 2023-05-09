# Solution

1. Create a new directory for your Docker image:

```bash
mkdir hello-world
cd hello-world
```

2. Create a new file called `Dockerfile` in the `hello-world` directory:

```bash
touch Dockerfile
```

3. Open the `Dockerfile` in a text editor and add the following lines:

```dockerfile
FROM alpine
RUN echo "Hello, World!"
CMD ["echo", "Hello, World!"]
```

4. Save and close the `Dockerfile`.

5. Build the Docker image using the `docker build` command:

```bash
docker build -t hello-world .
```
