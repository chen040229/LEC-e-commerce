from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()

def create_app():
    app = Flask(__name__, template_folder='templates')
    app.secret_key = '251005'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./testdb.db'


    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)

    from models import User

    @login_manager.user_loader
    def load_user(uid):
        return User.query.get(uid)
    
    bcrypt = Bcrypt(app)

    from login_routes import register_routes
    from prodcuts_routes import products_routes
    from person_routes import person_routes
    register_routes(app, db, bcrypt)
    app.register_blueprint(products_routes, url_prefix= "/products")
    app.register_blueprint(person_routes, url_prefix= "/person")

    migrate = Migrate(app,db)

    return app