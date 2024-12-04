# FastAPI with YubiKey OTP Authentication

## Install:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
poetry install
```

Server:

```bash
uvicorn app.server:app --reload
```

Client:
```bash
python -m app.client
```
