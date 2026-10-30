# Flask Git Assignment — Task 1 Starter

This starter contains the Flask project required for Task 1.

## Routes
- `GET /` — home page
- `GET /api` — reads and returns `data.json` as JSON

## Setup on Linux
```bash
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python app.py
```
Open `http://127.0.0.1:5000/` and `http://127.0.0.1:5000/api`.

For Tasks 3 and 4, add the To-Do page and MongoDB POST route on the requested feature branches.
