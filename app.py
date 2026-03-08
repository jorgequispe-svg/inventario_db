from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'tu_clave_secreta'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/inventario_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    # Registrar blueprints
    from views.producto import bp_producto
    from views.compra import bp_compra
    from views.venta import bp_venta
    from views.auth import auth_bp

    app.register_blueprint(bp_producto)
    app.register_blueprint(bp_compra)
    app.register_blueprint(bp_venta)
    app.register_blueprint(auth_bp)

    @app.route('/')
    def index():
        return "<h1>Sistema de Inventario</h1> <a href='/login'>Login</a> | <a href='/register'>Registrarse</a>"

    return app

app = create_app()

from models import User

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

if __name__ == '__main__':
    app.run(debug=True)