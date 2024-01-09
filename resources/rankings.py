from flask import request, jsonify
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from sqlalchemy import inspect
from database.models import db, Purchase, User, Product
import json

# User rakinkig

class RankingUsresAPI(Resource):
    @jwt_required()
    def get(self):
        top_users = db.session.query(
            User.full_name,
            db.func.sum(Purchase.price)\
                .label('total_sum')
            ).join(
                Purchase, User.id == Purchase.user_id
                ).group_by(User.full_name)\
                    .order_by(
                        db.func.sum(Purchase.price).desc()
                        ).all()
                        
        my_dict = {"User name":[],"total_sum":[]}
        for row in top_users:
            my_dict["User name"].append(row[0])
            my_dict["total_sum"].append(row[1])
        #print(my_dict)
        return jsonify(my_dict)

# Product ranking 

class RankingProductsAPI(Resource):
    @jwt_required()
    def get(self):
        top_product = db.session.query(
            Product.name,
            db.func.count(Purchase.bar_code)\
                .label('transactions')
            ).join(
                Purchase, Product.bar_code == Purchase.bar_code
                ).group_by(Product.name)\
                    .order_by(
                        db.func.count(Purchase.bar_code).desc()
                        ).all()
                        
        my_dict = {"Product name":[],"transactions":[]}
        for row in top_product:
            my_dict["Product name"].append(row[0])
            my_dict["transactions"].append(row[1])
        #print(my_dict)
        return jsonify(my_dict)