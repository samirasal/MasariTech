# General

_Note: you MUST have python 3.11 installed for this project to work._

## AI Scanning Model (OpenCV x Open3d)

### Activate the virtual environment

```bash
source virt/bin/activate
```

### Install dependencies

```bash
pip install -r requirements/<name>.txt
```

### Freezing dependencies (Only if you are adding new dependencies)

```bash
pip freeze > requirements/<name>.txt
```

### Deactivate the virtual environment

```bash
deactivate
```

# FastAPI (backend)

### Create a virtual environment

```bash
python3.11 -m venv venv_backend
```

### Activate the virtual environment

```bash
source venv_backend/bin/activate
```

### Run the server

```bash
cd backend
fastapi dev api_server.py
```

### Deactivate the virtual environment

```bash
deactivate
```
