from flask import request
from flask import jsonify
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask_jwt_extended import jwt_required, get_jwt_identity
import json
import datetime
from database.models import db, User

class SignupApi(Resource):
    def post(self):
        ## body = {email, password}
        body = request.get_json()
        user = User(
            full_name=body.get('full_name'),
            email=body.get('email'),
            password_hash=User.hash_password(body.get('password'))
        ) 
        try:
            db.session.add(user)
            db.session.commit()
            return jsonify(user)
        except Exception as e:
            print(e)
            return {'error': 'Couldnt register user because : %s' % e}, 400
   
class LoginApi(Resource):
    def post(self):
        ## body = {email, password}
        body = request.get_json()
        try:
            existing_user = User.query.filter(
                User.email == body.get('email')
            ).first()
            if existing_user == None:
                return {'error': 'Email or password invalid'}, 401
            authorized = existing_user.check_password(body.get('password'))
            if not authorized:
                return {'error': 'Email or password invalid'}, 401

            expires = datetime.timedelta(days=7)
            # Create a new token valid for 7
            access_token = create_access_token(identity=str(existing_user.id), expires_delta=expires)
            return {'token': access_token}, 200
        except Exception as e:
            print(e)
            return {'error': 'Couldnt login user because : %s' % e}, 400

class SessionAPI(Resource):
    @jwt_required()
    def get(self):
        try:
            # extract info from the jwt token
            user_id = get_jwt_identity()
            existing_user = User.query.filter(User.id == user_id).first()
            if existing_user == None:
                return {'error': 'User associated to token not found'}, 404
            return jsonify(existing_user)
        except Exception as e:
            print(e)
            return {'error': 'Internal error : %s' % e}, 500