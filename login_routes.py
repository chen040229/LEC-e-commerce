from flask import request, render_template, redirect, url_for, flash
from models import Product
from models import User
from flask_login import login_user, logout_user, current_user, login_required


def register_routes(app, db, bcrypt):

    @app.route('/', methods = ['GET','POST'])
    def index():
        return render_template('main.html')
    

    '''''
    @app.route('/products', methods = ['GET','POST'])
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
    
    @app.route('/delete/<id>', methods = ['DELETE'])
    def delete(id):
        Product.query.filter(Product.id == id).delete()
        db.session.commit()
        products = Product.query.all()
        return render_template('products.html', products = products )

    @app.route('/details/<id>', methods = ['GET'])
    def details(id):
        product = Product.query.filter(Product.id == id).first()
        return render_template('details.html', product = product)
    

    '''




    @app.route('/signup', methods = ['GET', 'POST'])
    def signup():
        if request.method == 'GET':
            return render_template('signup.html')
        elif request.method == "POST":
            username = request.form.get('username')
            password = request.form.get('password')
            confirm = request.form.get('comfirmpassword')

            if(password != confirm):
                flash(f'Password does not match!',category='danger')
                return redirect(url_for('signup'))
            

            hashed_password = bcrypt.generate_password_hash(password)
            user = User(username=username, password=hashed_password)

            db.session.add(user)
            db.session.commit()

            return redirect(url_for('index'))


    @app.route('/login', methods = ['GET', 'POST'])
    def login():
        if request.method == 'GET':
            return render_template('login.html')
        elif request.method == 'POST':
            username = request.form.get('username')
            password = request.form.get('password')


            user = User.query.filter(User.username == username).first()


            if user is None:
                return "Username not found, please sign up first or check your username."

            if bcrypt.check_password_hash(user.password, password):
                login_user(user)
                flash(f'Welcome! Let us LEC!',category='success')
                return redirect(url_for('products.add'))
            else:
                return 'Failed'
    
    @app.route('/logout')
    def logout():
        logout_user()
        return redirect(url_for('index'))
    
    @app.route('/clear')
    def clear():
        User.query.delete()
        db.session.commit()

        return redirect(url_for('index'))