from flask import Flask
from config import config
from routes import init_routes
from flask_restful import Api
from auth.auth import init_jwt

# ===== STARTING FLASK APP =====
app = Flask(__name__)

# ===== APP CONFIGURATIONS =====
app.config["JWT_SECRET_KEY"] = "super-secret"
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 300

# ===== INIT JWT =====
init_jwt(app)

# ===== INIT API ROUTES =====
api = Api(app)
init_routes(api)


if __name__ == '__main__':
    app.config.from_object(config['development'])
    #app.register_error_handler(404, page_not_found)
    app.run()






