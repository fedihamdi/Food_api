from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import generate_password_hash, check_password_hash
from dataclasses import dataclass




db = SQLAlchemy()

@dataclass
class User(db.Model):
    ## For API JSON reponse
    id: int
    email: str
    full_name: str
    ##

    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    full_name = db.Column(db.String())
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(), nullable=False)

    ## Auto generated timestamps for creation & update of the row
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    ## Method to instanciate class (doesnt save in the database)
    def __init__(self, full_name, email, password_hash):
        self.full_name = full_name
        self.email = email
        self.password_hash = password_hash

    ## Method to print the class in the terminal: print(User)
    def __repr__(self):
        return f"<User ({self.id}): {self.email}>"

    ## Method to hash a password with Bcrypt
    @staticmethod
    def hash_password(password):
        return generate_password_hash(password).decode('utf8')
 
    ## Method to compare a password with an hashed string
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@dataclass
class Product(db.Model):
    ## For API JSON reponse
    bar_code: str
    name: str
    nutri_score: str
    brand: str
    created_at: datetime
    updated_at: datetime
    ##

    __tablename__ = 'products'

    bar_code = db.Column(db.String(), primary_key=True)
    name = db.Column(db.String(), nullable=False, unique=True)
    nutri_score = db.Column(db.String())
    brand = db.Column(db.String())

    ## Auto generated timestamps for creation & update of the row
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, bar_code, name, nutri_score, brand):
        self.bar_code = bar_code
        self.name = name
        self.nutri_score = nutri_score
        self.brand = brand

    def __repr__(self):
        return f"<Product {self.name} with bar code {self.bar_code}>"


@dataclass
class Purchase(db.Model):
    ## For API JSON reponse
    id: int
    bar_code : str
    user_id : str
    price : int
    created_at: datetime
    updated_at: datetime
    ##

    __tablename__ = 'purchases'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    bar_code = db.Column(db.String(), db.ForeignKey('products.bar_code'),nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'),nullable=False)
    price = db.Column(db.Integer)

    ## Auto generated timestamps for creation & update of the row
    
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, server_default=db.func.now(), server_onupdate=db.func.now())

    def __init__(self, bar_code, user_id, price):
        self.bar_code = bar_code
        self.user_id = user_id
        self.price = price

    def __repr__(self):
        return f"<Purchase by user {self.user_id} for product with bar code {self.bar_code}>"

