from flask_jwt_extended import jwt_required
from flask_restful import Resource, reqparse
from product.product import Product

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, required=True, help="Cannot be blank")
parser.add_argument('description', type=str, required=True, help="Cannot be blank")
parser.add_argument('price', type=float, required=True, help="Only accepts double type")

class ProductListResource(Resource):
    @jwt_required()
    def get(self):
        products = Product.get_all()
        return [product.to_dict() for product in products], 200

    @jwt_required()
    def post(self):
        args = parser.parse_args()
        new_product = Product(name=args['name'], description=args.get('description'), price=args['price'])
        new_product.save()
        return new_product.to_dict(), 201

class ProductResource(Resource):
    @jwt_required()
    def get(self, id):
        product = Product.get_by_id(id)

        if product:
            return product.to_dict(), 200
        else:
            return {"message":"Item Not found"},404

    @jwt_required()
    def put(self, id):
        product = Product.get_by_id(id)

        if not product:
            return {'message':'Product not found!'}, 404

        args = parser.parse_args()
        product.name = args.get('name', product.name)
        product.description = args.get('description', product.description)
        product.price = args.get('price', product.price)
        product.save()

        return product.to_dict(), 200

    @jwt_required()
    def delete(self, id):
        product = Product.get_by_id(id)

        if not product:
            return {'message': 'Product not found!'}

        product.delete()
        return '', 204


