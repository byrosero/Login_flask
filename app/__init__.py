from flask import Flask, render_template
from config import Config
from .models import db, User
from flask_jwt_extended import JWTManager
from flask_cors import CORS 

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    app.config["JWT_SECRET_KEY"] = Config.SECRET_KEY

    db.init_app(app)
    jwt = JWTManager(app)

    #CONFIGURACIÓN CORS 
    CORS(app, resources={
        r"/*": {
            "origins": "http://localhost:4200"
        }
    })

    from .routes import api
    app.register_blueprint(api)

    with app.app_context():
        db.create_all()

    @app.route('/')
    def index():
        return render_template('index.html')

    return app