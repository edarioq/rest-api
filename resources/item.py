from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.item import ItemModel

class Item(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('price',
        type=float,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('store_id',
        type=int,
        required=True,
        help="Every item needs a store ID."
    )

    @jwt_required()
    def get(self, name):
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()

        return { 'message': 'Item not found'}, 404

    def post(self, name):
        if ItemModel.find_by_name(name):
            msg = "An item with that name '{}' already exists.".format(name)
            return { 'message': msg }, 400

        data = Item.parser.parse_args()
        item = ItemModel(name, data['price'], data['store_id'])

        try:
            item.save()
        except:
            return { 'message': 'An error occured!' }, 500

        return { 'status': 'Item created.', 'item': item.json() }, 201

    def delete(self, name):
        item = ItemModel.find_by_name(name)

        if item:
            item.delete()

        return { 'message': 'Item deleted' }

    def put(self, name):
        data = Item.parser.parse_args()

        item = ItemModel.find_by_name(name)

        if item is None:
            try:
                item = ItemModel(name, data['price'], data['store_id'])
                return { 'message': 'Created', 'item': item }
            except:
                return { 'message': 'Can\'t insert the item.' }, 500
        else:
            try:
                item.price = data['price']
                item.id = data['store_id']
            except:
                return { 'message': 'Can\'t update the item.' }, 500

        item.save()

        return { 'message': 'Updated', 'item': item.json() }


class ItemList(Resource):
    def get(self):
        items = list(map(lambda x: x.json(), ItemModel.query.all()))

        return { 'items': items }, 200
