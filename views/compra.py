from flask import Blueprint, render_template, request, redirect, url_for
from models import Compra, Producto
from app import db
from flask_login import login_required

bp_compra = Blueprint('compra', __name__, url_prefix='/compra')

@bp_compra.route('/')
@login_required
def listar():
    compras = Compra.query.all()
    return render_template('compras.html', compras=compras)

@bp_compra.route('/nueva', methods=['GET', 'POST'])
@login_required
def nueva():
    productos = Producto.query.all()
    if request.method == 'POST':
        producto_id = int(request.form['producto_id'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = float(request.form['precio_unitario'])
        compra = Compra(producto_id=producto_id, cantidad=cantidad, precio_unitario=precio_unitario)
        # Actualizar stock del producto
        producto = Producto.query.get(producto_id)
        producto.stock += cantidad
        db.session.add(compra)
        db.session.commit()
        return redirect(url_for('compra.listar'))
    return render_template('nueva_compra.html', productos=productos)