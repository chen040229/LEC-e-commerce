from app import db
from flask_login import UserMixin
class User(db.Model, UserMixin):
  __tablename__ = "users"
  uid = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String, nullable = False)
  password = db.Column(db.String, nullable = False)
  email = db.Column(db.String(255), nullable=True)
  number = db.Column(db.String(255), nullable=True)
  description = db.Column(db.String)


  def __repr__(self):
    return f"<User: {self.username}>"

  def get_id(self):
    return self.uid
  
class Product(db.Model):
  __tablename__ = "products"
  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(100), nullable=False)
  price = db.Column(db.Integer, nullable=False)
  description = db.Column(db.String(255), nullable=False)
  original_price = db.Column(db.Integer, nullable=False)
  quantity = db.Column(db.Integer, nullable=False)
  new_level  = db.Column(db.Integer, nullable=False)

  
  def __repr__(self):
    return f"<Product {self.id} {self.name} {self.price} {self.email}>"
  

class Need(db.Model):
  __tablename__ = "needs"
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.String(100), nullable=False)
  description = db.Column(db.String(255), nullable=False)

  
  def __repr__(self):
    return f"<Need {self.id} {self.name} {self.price}>"