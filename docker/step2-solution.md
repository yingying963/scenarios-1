# Solution

1. Create a new directory for your Docker image:

```bash
mkdir flask-app
cd flask-app
```

2. Create a new file called `Dockerfile` in the `flask-app` directory:

```bash
touch Dockerfile
```

3. Open the `Dockerfile` in a text editor and add the following lines:

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
```

4. Save and close the `Dockerfile`.

5. Create a new file called `requirements.txt` in the `flask-app` directory:

```bash
touch requirements.txt
```

6. Open the `requirements.txt` file in a text editor and add the following line:

```bash
Flask==1.1.2
```

7. Save and close the `requirements.txt` file.

8. Build the Docker image using the `docker build` command:

```bash
docker build -t flask-app .
```
