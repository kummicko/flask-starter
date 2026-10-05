"""Run the app in a native desktop window (optional: needs the `desktop` extra)."""
import webview

from . import create_app


def main() -> None:
    app = create_app()
    webview.create_window("Flask Starter", app, width=1000, height=700)
    webview.start()


if __name__ == "__main__":
    main()
