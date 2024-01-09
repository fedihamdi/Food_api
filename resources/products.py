from flask import request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from services.open_food_fact import open_food_fact
from database.models import db, Product, Purchase
    
class ProductAPI(Resource):
    @jwt_required()
    def get(self, bar_code):
        existing_product = Product.query.filter(Product.bar_code == bar_code).first()

        if existing_product == None:
            try:
                open_fd_product = open_food_fact.get_product_by_code(bar_code)
                prod = Product(
                    bar_code = open_fd_product["code"],
                    name = open_fd_product["product"]["product_name"],
                    brand = open_fd_product["product"]["brands"],
                    nutri_score = open_fd_product["product"]["nutriscore_score"]
                )
                
                db.session.add(prod)
                db.session.commit()
                return jsonify(existing_product)
            except Exception as e:

                print(e)
                return {'error': 'open product because: %s' % e}, 400
            
            #return {'error': "Product with code %s not found it will be added and this is the product added" % bar_code }, 404

        existing_product = Product.query.filter(Product.bar_code == bar_code).first()
        return jsonify(existing_product)

class ProductsAPI(Resource):
    @jwt_required()
    def get(self):
        products = Product.query.all()

        return jsonify(products)




