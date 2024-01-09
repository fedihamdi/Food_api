from genericpath import exists
from flask import request
from flask import jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource
from services.open_food_fact import open_food_fact
from database.models import db, Product, Purchase
import requests


class PurchaseAPI(Resource):
    @jwt_required()
    def post(self):
        body = request.get_json()
        bar_code = body.get('bar_code')
        price = body.get('price')
        if bar_code == None or (float(price) < 0 or float(price) > 99999):
            return {'error': 'bar code does not exist or price must be between 0 and 99999'}, 400
        user_id = get_jwt_identity()
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

            except Exception as e:

                print(e)
                return {'error': 'open product because: %s' % e}, 400
        purchase = Purchase(
            bar_code = body.get('bar_code'),
            user_id = user_id,
            price = body.get('price')
        )
        db.session.add(purchase)
        db.session.commit()
        return jsonify(purchase)