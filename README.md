# Flask Starter

A starter for Flask projects: **uv** for dependencies, a **src layout** with
a blueprint structure, **Tailwind CSS + daisyUI** (no Node), and an optional
**pywebview** desktop window.

```
src/app/
├── __init__.py          # create_app() + register_blueprints()
├── desktop.py           # optional pywebview launcher
├── blueprints/main/     # __init__.py (bp) + routes.py
├── templates/           # base.html, main/index.html
└── static/css/          # input.css (+ tailwindcss binary, daisyUI, output.css after setup)
```

## Quick start

```bash
uv sync
cp .env.example .env     # then set a real FLASK_SECRET_KEY

# Tailwind CLI + daisyUI (Linux / macOS)
cd src/app/static/css && curl -sL daisyui.com/fast | bash && cd -
# Windows (PowerShell)
# cd src/app/static/css; irm daisyui.com/fast.ps1 | iex
```

The daisyUI script downloads the `tailwindcss` binary and daisyUI into
`src/app/static/css/` and builds `output.css`. Those files are gitignored.
`input.css` is committed; if the script overwrites it, that's fine.

## Running

Use two terminals, both from the project root.

**1. CSS watcher** (rebuilds `output.css` when templates change):
```bash
src/app/static/css/tailwindcss -i src/app/static/css/input.css -o src/app/static/css/output.css --watch
```
Use `--minify` instead of `--watch` for a production build.

**2a. Browser mode** (default, with auto-reload):
```bash
uv run flask --app app run --debug
```

**2b. Desktop mode** (optional, see below):
```bash
uv run --extra desktop desktop
# or: uv run --extra desktop python -m app.desktop
```

## Optional: desktop mode (pywebview)

Wraps the Flask app in a native window. It's an optional dependency group
called `desktop`, so projects that don't need it never install it.

Enable it per project:
```bash
uv sync --extra desktop
```

**Linux** uses the GTK backend (lighter than Qt) and needs system packages
first. On Debian/Ubuntu:
```bash
sudo apt install pkg-config python3-dev libcairo2-dev libgirepository1.0-dev \
  gir1.2-gtk-3.0 gir1.2-webkit2-4.1
```
**Windows / macOS** use the system webview, so there's nothing extra to install.

Notes:
- Build the CSS before launching; the window just loads `output.css`.
- Keep developing in browser mode for auto-reload, and use the window to test.
- Don't write user data next to the code: once packaged that folder may be read-only.
- Don't want desktop mode in a project? Delete `src/app/desktop.py`, the
  `desktop` extra and the `[project.scripts]` block in `pyproject.toml`.

## Adding a blueprint

1. Create `src/app/blueprints/<name>/` with `__init__.py` and `routes.py`:
   ```python
   # __init__.py
   from flask import Blueprint
   bp = Blueprint("<name>", __name__, url_prefix="/<name>")
   from . import routes
   ```
   ```python
   # routes.py
   from flask import render_template
   from . import bp

   @bp.get("/")
   def index():
       return render_template("<name>/index.html")
   ```
2. Add templates in `src/app/templates/<name>/` extending `base.html`.
3. Register it in `register_blueprints()` in `src/app/__init__.py`:
   ```python
   from .blueprints.<name> import bp as <name>_bp
   app.register_blueprint(<name>_bp)
   ```

Every blueprint can name its variable `bp`; only the string passed to
`Blueprint()` must be unique. Alias them on import (`as <name>_bp`).

## Using this as a template

On GitHub, tick **Settings → General → Template repository**, then:

```bash
gh repo create my-new-app --private --template YOUR_USER/flask-starter --clone
cd my-new-app
```

Per-project checklist:
1. Change `name` (and `description`) in `pyproject.toml`.
2. Change the titles in `templates/base.html` and `desktop.py`.
3. `uv sync` (add `--extra desktop` if needed).
4. Run the daisyUI install script (see Quick start).
5. `cp .env.example .env` and set a real `FLASK_SECRET_KEY`.

The `src/app` package is deliberately generic, so `flask --app app run` and all
imports keep working in every project without renaming.

## Contributing and license

Contributions are welcome, see [CONTRIBUTING.md](CONTRIBUTING.md).
Released under the [MIT License](LICENSE).
