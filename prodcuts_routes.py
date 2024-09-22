from flask import request, render_template, redirect, Blueprint, url_for
from models import Product
from app import db

products_routes = Blueprint("products", __name__, template_folder="templates")


        
@products_routes.route('/', methods = ['GET','POST'])
def add():
    if request.method == "GET":
        products = Product.query.all()
        return render_template('products.html', products = products )
    elif request.method == "POST":
        id = request.form.get('id')
        name = request.form.get('name')
        price = request.form.get('price') + "$"
        description = request.form.get('description')
        original_price = request.form.get('original_price') + "$"
        quantity = request.form.get('quantity')
        new_level = request.form.get('new_level') + "%"
        

        product = Product(id=id, name=name,price=price,description=description,
                            original_price=original_price, quantity=quantity,
                            new_level=new_level)

        db.session.add(product)
        db.session.commit()

        products = Product.query.all()
        return render_template('products.html', products = products )

@products_routes.route('/delete/<id>', methods = ['DELETE'])
def delete(id):
    Product.query.filter(Product.id == id).delete()
    db.session.commit()
    products = Product.query.all()
    return render_template('products.html', products = products )

@products_routes.route('/details/<id>', methods = ['GET'])
def details(id):

    product = Product.query.filter(Product.id == id).first()
    return render_template('details.html', product = product)