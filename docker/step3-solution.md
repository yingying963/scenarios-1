# Solution

1. Create a new directory for your Docker image:

```bash
mkdir flask-app-env
cd flask-app-env
```

2. Create a new file called `Dockerfile` in the `flask-app-env` directory:

```bash
touch Dockerfile
```

3. Open the `Dockerfile` in a text editor and add the following lines:

```dockerfile
FROM python:3.7-alpine
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
ENV PORT=5000
```

4. Save and close the `Dockerfile`.

5. Create a new file called `requirements.txt` file in a text editor and add the following line:

```bash
Flask==1.1.2
```

6. Create a new file called `app.py` in the `flask-app-env` directory:

```bash
touch app.py
```

7. Open the `app.py` file in a text editor and add the following lines:

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

8. Save and close the `app.py` file.

9. Build the Docker image using the `docker build` command:

```bash
docker build -t flask-app-env .
```
