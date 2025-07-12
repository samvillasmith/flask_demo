# Flask Demo 🧪

A collection of **tiny, self‑contained Flask apps** that demonstrate everyday web‑engineering tasks: classic MVC pages, JSON APIs, HTML form handling and Jinja templating.  Each script is fewer than \~60 lines, so you can inspect patterns quickly or copy‑paste them into new projects.

> **What a hiring manager can find here**
> • Flask fundamentals (blueprints, routing, request/response cycle).
> • REST API conventions & error handling.
> • Jinja templating & static page delivery.
> • Clean project hygiene (requirements file, docstrings, runnable in <10 min).

---

## 📁 Project layout

```
flask_demo/
├── flask/
│   ├── app.py            # "Hello world" root & index demo
│   ├── api.py            # CRUD JSON API with in‑memory list
│   ├── getpost.py        # Classic GET + POST form example
│   ├── jinja.py          # Templating, URL params + conditional rendering
│   ├── main.py           # Minimal site with Index & About pages
│   └── templates/
│       ├── index.html
│       ├── about.html
│       ├── form.html
│       ├── result*.html  # output pages for jinja.py examples
│       └── ...
├── requirements.txt      # Flask 3.x + simplejson
└── README.md             # ← you are here
```

---

## 🚀 Quick‑start (local)

```bash
# clone
 git clone https://github.com/youruser/flask_demo.git && cd flask_demo

# create isolated env – venv shown; substitute Conda/Mamba if preferred
 python -m venv .venv && source .venv/bin/activate        # Windows: .venv\Scripts\activate

# install dependencies
 pip install -r requirements.txt

# run a demo of choice
 # 1️⃣ Basic welcome
 python flask/app.py             # http://127.0.0.1:5000/

 # 2️⃣ JSON API with CRUD
 python flask/api.py             # use curl/Postman against http://127.0.0.1:5000/items

 # 3️⃣ Forms + templates
 python flask/getpost.py         # open http://127.0.0.1:5000/form
```

All apps run on **Python 3.11+** and bind to `localhost:5000` with `debug=True` so you get auto‑reload.

---

## 🛣️ API reference (`api.py`)

| Method     | Endpoint      | Purpose              | Body / Params                                       |
| ---------- | ------------- | -------------------- | --------------------------------------------------- |
| **GET**    | `/`           | Health check         | –                                                   |
| **GET**    | `/items`      | List all items       | –                                                   |
| **GET**    | `/items/<id>` | Retrieve single item | Path param `id` (int)                               |
| **POST**   | `/items`      | Create item          | JSON `{ "name": str, "price": float }`              |
| **PUT**    | `/items`      | Update item          | JSON `{ "id": int, "name": str?, "price": float? }` |
| **DELETE** | `/items/<id>` | Delete item          | Path param `id` (int)                               |

Responses are `application/json`; errors return an `error` message + appropriate HTTP status.

---

## ✨ What to look for in the code

* **Idiomatic Flask** – `@app.route` decorators, blueprint‑ready structure, `debug=True` for dev.
* **Type‑annotated helpers** – functions in `api.py` are hinted for readability.
* **Thin views** – logic stays small; heavy lifting would normally move into a service layer.
* **Jinja templates** – loops, conditionals and filters (see `result*.html`).

---

## 🤹‍♂️ Next steps (stretch goals)

* [ ] Convert apps into **Flask blueprints** and register via factory pattern.
* [ ] Add **pytest** + GitHub Actions CI badge.
* [ ] Dockerise (`Dockerfile`, `docker compose up`) for one‑command ops.
* [ ] Swap in **SQLAlchemy** with SQLite so `api.py` persists data.

---

## 📝 License

MIT – use these snippets in personal or commercial work. Attribution appreciated.

*Last updated July 2025*
