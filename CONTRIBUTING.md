# Contributing to flask-starter

Thanks for helping out! This is a small starter template, so the goal is to
keep it **minimal, clear and easy to reuse**. Bug fixes, docs improvements and
small quality-of-life changes are all welcome.

## Ways to contribute

- Report a bug or unclear instruction by opening an issue.
- Improve the README or setup steps (especially for macOS and Windows).
- Pick up an issue labelled **good first issue**.
- Suggest a feature. Please open an issue first so we can agree it fits the
  starter before you spend time on it.

## What fits (and what doesn't)

The starter intentionally ships without a database, authentication or an ORM.
Those vary per project, so changes that add them to the template itself will
likely be declined. Ideas like that are better as a separate branch or a
documented recipe in the README.

Good fits:
- Fixes to the project structure, the blueprint pattern or the Tailwind/daisyUI setup
- Cross-platform improvements (Linux, macOS, Windows)
- Clearer docs and comments
- Small, optional conveniences that don't add required dependencies

## Development setup

You need [uv](https://docs.astral.sh/uv/) and Python 3.12 or newer.

```bash
git clone https://github.com/kummicko/flask-starter.git
cd flask-starter
uv sync
cp .env.example .env

# Tailwind CLI + daisyUI (Linux / macOS)
cd src/app/static/css && curl -sL daisyui.com/fast | bash && cd -
```

On Windows, use the PowerShell command from the README instead.

Run the CSS watcher and the app in two terminals:

```bash
src/app/static/css/tailwindcss -i src/app/static/css/input.css -o src/app/static/css/output.css --watch
uv run flask --app app run --debug
```

### Desktop mode (optional)

Only needed if you're changing `src/app/desktop.py`:

```bash
uv sync --extra desktop
uv run --extra desktop desktop
```

On Linux this needs GTK system packages. See the README for the list.

## Making a change

1. Fork the repo and create a branch from `main`:
   ```bash
   git checkout -b fix/short-description
   ```
2. Make your change. Keep it focused: one topic per pull request.
3. Run the app and check the pages you touched in the browser. If you changed
   styling, make sure the CSS still builds without errors.
4. If you changed setup steps, dependencies or behaviour, update the README.
5. Commit with a clear message in the imperative mood, for example
   `Fix Windows install command in README`.
6. Push your branch and open a pull request. Describe what changed and why, and
   mention your OS if the change is platform-specific.

## Code style

- Follow standard Python style (PEP 8) and keep functions small and readable.
- Keep the blueprint pattern consistent: each blueprint lives in
  `src/app/blueprints/<name>/` with its own `__init__.py` (defining `bp`) and
  `routes.py`, and templates in `src/app/templates/<name>/`.
- Put dependencies in `pyproject.toml` with `uv add` (or `uv add --optional`
  for extras) so `uv.lock` stays in sync. Commit the updated `uv.lock`.
- Don't commit generated or downloaded files: the `tailwindcss` binary,
  `daisyui*.mjs`, `output.css`, `.venv` and `.env` are all gitignored.

## Reporting bugs

Please include:
- What you did and what you expected to happen
- What actually happened, with the full error message if there is one
- Your OS, Python version (`python --version`) and uv version (`uv --version`)

## License

By contributing, you agree that your contributions will be licensed under the
[MIT License](LICENSE).
