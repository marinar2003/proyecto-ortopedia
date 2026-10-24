from flask import Flask


def create_app():
    """Crea y configura la aplicación Flask (patrón application factory)."""
    app = Flask(__name__)

    from app.routes import main
    app.register_blueprint(main)

    return app
