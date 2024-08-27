from user.resources import UserListResource
from product.resources import ProductListResource,ProductResource
from auth.resources import  AuthResource, LogoutResource

def init_routes(api):
    # ROUTES FOR PRODUCTS API
    api.add_resource(ProductListResource, "/api/v1/products")
    api.add_resource(ProductResource, "/api/v1/products/<int:id>")

    # # ROUTES FOR USERS API
    api.add_resource(UserListResource, "/api/v1/users")

    # ROUTES FOR AUTH API
    api.add_resource(AuthResource, "/api/v1/auth")
    api.add_resource(LogoutResource, "/api/v1/auth/logout")
