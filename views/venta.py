from flask import Blueprint, render_template, request, redirect, url_for
from models import Venta, Producto
from app import db
from flask_login import login_required

bp_venta = Blueprint('venta', __name__, url_prefix='/venta')

@bp_venta.route('/')
@login_required
def listar():
    ventas = Venta.query.all()
    return render_template('ventas.html', ventas=ventas)

@bp_venta.route('/nueva', methods=['GET', 'POST'])
@login_required
def nueva():
    productos = Producto.query.all()
    if request.method == 'POST':
        producto_id = int(request.form['producto_id'])
        cantidad = int(request.form['cantidad'])
        precio_unitario = float(request.form['precio_unitario'])
        producto = Producto.query.get(producto_id)
        if producto.stock >= cantidad:
            venta = Venta(producto_id=producto_id, cantidad=cantidad, precio_unitario=precio_unitario)
            # Actualizar stock
            producto.stock -= cantidad
            db.session.add(venta)
            db.session.commit()
            return redirect(url_for('venta.listar'))
        else:
            flash('Stock insuficiente')
    return render_template('nueva_venta.html', productos=productos)