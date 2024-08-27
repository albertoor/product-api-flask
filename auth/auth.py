from flask_jwt_extended import JWTManager,create_access_token, get_jwt
from user.user import User
from werkzeug.security import check_password_hash

jwt = JWTManager()
blacklist = set()

def init_jwt(app):
    jwt.init_app(app)

    @jwt.token_in_blocklist_loader
    def check_if_token_in_blacklist(jwt_header, jwt_payload):
        jti = jwt_payload['jti']
        return jti in blacklist

def authenticate(username, password):
    user = User.get_by_username(username)
    if user and check_password_hash(user.password, password):

        access_token = create_access_token(identity={'username': username})
        return access_token
    return None

