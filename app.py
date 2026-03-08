from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

app = Flask(__name__)
app.config['SECRET_KEY'] = 'tu_clave_secreta'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3306/db_reposteria'


# inicializaciones
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
admin = Admin(app, name='Inventario', template_mode='bootstrap3')

# Cargar usuario
from models import User, Producto, Compra, Venta

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Registrar vistas admin
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Producto, db.session))
admin.add_view(ModelView(Compra, db.session))
admin.add_view(ModelView(Venta, db.session))

@app.route('/')
def index():
    return render_template('index.html')  # Crear plantilla simple

if __name__ == '__main__':
    app.run(debug=True)