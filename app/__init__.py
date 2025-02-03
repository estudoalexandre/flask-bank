from flask import Flask
from app.config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()





def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)


    db.init_app(app)
    migrate.init_app(app, db)

    login_manager.init_app(app)
    login_manager.login_view = 'main.login'

    from app.models.cliente import Cliente
    @login_manager.user_loader
    def load_user(id):
        return Cliente.query.get(int(id))

    from app.routes import bp
    app.register_blueprint(bp)
    with app.app_context():
        from app import signals

    return app