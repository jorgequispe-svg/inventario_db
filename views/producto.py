from flask import Blueprint, render_template, request, redirect, url_for
from models import Producto
from app import db
from flask_login import login_required

bp_producto = Blueprint('producto', __name__, url_prefix='/producto')

@bp_producto.route('/')
@login_required
def listar():
    productos = Producto.query.all()
    return render_template('productos.html', productos=productos)

@bp_producto.route('/nuevo', methods=['GET', 'POST'])
@login_required
def nuevo():
    if request.method == 'POST':
        nombre = request.form['nombre']
        descripcion = request.form['descripcion']
        stock = int(request.form['stock'])
        precio = float(request.form['precio'])
        producto = Producto(nombre=nombre, descripcion=descripcion, stock=stock, precio=precio)
        db.session.add(producto)
        db.session.commit()
        return redirect(url_for('producto.listar'))
    return render_template('nuevo_producto.html')

@bp_producto.route('/editar/<int:id>', methods=['GET', 'POST'])
@login_required
def editar(id):
    producto = Producto.query.get_or_404(id)
    if request.method == 'POST':
        producto.nombre = request.form['nombre']
        producto.descripcion = request.form['descripcion']
        producto.stock = int(request.form['stock'])
        producto.precio = float(request.form['precio'])
        db.session.commit()
        return redirect(url_for('producto.listar'))
    return render_template('editar_producto.html', producto=producto)

@bp_producto.route('/eliminar/<int:id>')
@login_required
def eliminar(id):
    producto = Producto.query.get_or_404(id)
    db.session.delete(producto)
    db.session.commit()
    return redirect(url_for('producto.listar'))