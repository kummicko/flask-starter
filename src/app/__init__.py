from flask import Flask

from .blueprints.main import bp as main_bp


def create_app(config: dict | None = None) -> Flask:
    app = Flask(__name__)
    app.config.from_mapping(SECRET_KEY="dev")
    app.config.from_prefixed_env()  # e.g. FLASK_SECRET_KEY=...
    if config:
        app.config.update(config)

    register_blueprints(app)
    return app


def register_blueprints(app: Flask) -> None:
    # Add new blueprints here
    app.register_blueprint(main_bp)
