from flask import jsonify
from flask import request
from flask_restful import Resource
from datetime import datetime
from database.models import db, User

# /users routes
class UsersApi(Resource):
    def get(self):
        # The jsonify module will transforms python
        # dict to JSON objects (not needed for strings, numbers)
        users = User.query.all()
        return jsonify(users)

    def delete(self):
        try:
            num_rows_deleted = db.session.query(User).delete()
            db.session.commit()
            return {'message': '%d users were deleted' % num_rows_deleted}, 200
        except:
            db.session.rollback()
            return {'error': 'Couldnt delete all users'}, 422

# /users/<userId> routes
class UserApi(Resource):
    def get(self, userId):
        # filters the users and get the first item with next
        existing_user = User.query.filter(User.id == userId).first()
        if existing_user == None:
            return {'error': 'User with id %s not found' % userId}, 404
        return jsonify(existing_user)

    def delete(self, userId):
        try:
            existing_user = User.query.filter_by(id=userId).first()
            if existing_user == None:
                return {'error': 'User with id %s not found' % userId}, 404
            db.session.delete(existing_user)
            db.session.commit()
        except Exception as e:
            print(e)
            return {'error': 'Couldnt delete user because : %s' % e}, 400
        return {'message': 'User with id %s was deleted' % userId}, 200
