from flask import Flask, request, render_template, jsonify
from exts import db
import settings
from .views import bp

def create_app():
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(settings.DevelopmentConfig)
    app.register_blueprint(bp)

    db.init_app(app=app)

    return app
