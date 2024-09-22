from flask import request, render_template, redirect, url_for, Blueprint
from models import Product
from app import db

person_routes = Blueprint("person", __name__, template_folder="templates")


@person_routes.route('/', methods = ['GET','POST'])
def index():
    if request.method == "GET":
        return render_template('person.html')
    elif request.method == "POST":
        id = request.form.get('id')
        name = request.form.get('name')
        email = request.form.get('email')
        number = request.form.get('number')
        price = request.form.get('price') + "$"
        description = request.form.get('description')
        original_price = request.form.get('original_price') + "$"
        quantity = request.form.get('quantity')
        new_level = request.form.get('new_level') + "%"
        print(f"email: %s", email)
        

        product = Product(id=id, name=name,email=email,number=number,price=price,description=description,
                            original_price=original_price, quantity=quantity,
                            new_level=new_level)

        db.session.add(product)
        db.session.commit()

        products = Product.query.all()
        return render_template('products.html', products = products )