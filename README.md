# Flask To-Do App

To-do list with **Flask**, **SQLite**, **SQLAlchemy**, **Flask-Login**, and **Bootstrap 5**.

## Run

```bash
cd "path/to/to-do app"
python -m venv venv
```

Activate the venv, then:

```bash
pip install -r requirements.txt
python app.py
```

Open **http://127.0.0.1:5000/** . SQLite **`todo.db`** is created on first run.

Optional: `flask --app app init-db`

## Files

| File | Role |
|------|------|
| `app.py` | App factory, Flask-Login, registers blueprints |
| `auth.py` | Auth blueprint (register, login, logout) |
| `tasks.py` | Tasks blueprint (list + CRUD) |
| `models.py` | `User`, `Task`, `db` |
| `templates/` | HTML templates |
| `static/style.css` | Extra styles |

## License

Use freely for learning or your own projects.
