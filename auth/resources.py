from flask_jwt_extended import jwt_required, get_jwt
from flask_restful import Resource
from flask import request
from auth.auth import authenticate, blacklist


class AuthResource(Resource):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        access_token = authenticate(username, password)

        if access_token:
            return {'access_token': access_token}, 200
        return {'message': 'Bad username or password'}, 401

class LogoutResource(Resource):
    @jwt_required()
    def post(self):
        jwt_data = get_jwt()
        jti = jwt_data['jti']
        blacklist.add(jti)
        return {'message':'Logged out successfully!'},200
