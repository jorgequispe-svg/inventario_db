from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_admin import Admin
from flask_migrate import Migrate

db = SQLAlchemy()
login_manager = LoginManager()
admin = Admin(name="Panel Administrador", template_mode='bootstrap3')
migrate = Migrate()