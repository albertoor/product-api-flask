from flask_restful import Resource, reqparse
from user.user import User
from werkzeug.security import generate_password_hash

parser = reqparse.RequestParser()
parser.add_argument('username', type=str, required=True, help="Cannot be blank")
parser.add_argument('password', type=str, required=True, help="Cannot be blank")

class UserListResource(Resource):
    @staticmethod
    def get():
        users = User.get_all()
        return [user.to_dict() for user in users], 200

    def post(self):
        args = parser.parse_args()
        username = args['username']
        password = args['password']

        password_hash = generate_password_hash(password)

        new_user = User(username=username, password=password_hash)
        new_user.save()
        return new_user.to_dict(), 201
