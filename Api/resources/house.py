from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from models.house import HouseModel
from models.user import UserModel
import json
from flask_jwt_extended import jwt_required

class House(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('location_word', type=str)
    parser.add_argument('number_of_bedrooms', type=int)
    # parser.add_argument('image_cover')
    parser.add_argument('rent_amount_per_month', type=float)
    parser.add_argument('area_in_square_meter', type=float)
    parser.add_argument('description', type=str)
    parser.add_argument('coordinates')

    def get(self, id):
        house = HouseModel.find_by_id(id)
        if house:
            return house.json()
        return {
            'status': 'failed',
            'message': 'house not found'}, 400

    # @jwt_required
    def delete(self, id):
        house = HouseModel.find_by_id(id)
        if house:
            house.delete_from_db()
            return {'message': 'house deleted.'}, 201
        return {'message': 'house id is invalid.'}, 404

    def put(self, id):
        
        data = House.parser.parse_args()

        house = HouseModel.find_by_id(id)
        # print(data)

        # for row in data.keys():s
        #     if data[row] = None:
        #         print (row, data[row])
        #     else:
        #         house.

        # if house:
        #     HouseModel.update_by_id(id, data)

        #     return{
        #         'status': 'success',
        #         'data': house.json()
        #     }

        return {'message': 'house id is invalid.'}, 404



class HouseList(Resource):
    parser = reqparse.RequestParser()

    def get(self):
        return {'houses': list(map(lambda x: x.json(), HouseModel.query.all()))}
    @jwt_required()
    def post(self):
        
        parser.add_argument('location_word', type=str, required=True, help="A house must have a location!!")
        parser.add_argument('number_of_bedrooms', type=int, required=True, help="A house must have number of bedrooms")
        # parser.add_argument('image_cover')
        parser.add_argument('rent_amount_per_month', type=float, required=True, help="A house must habe the rent amount")
        parser.add_argument('area_in_square_meter', type=float)
        parser.add_argument('description', type=str)
        parser.add_argument('coordinates')

        data = parser.parse_args()
        print({**data})


        current_user = UserModel.find_by_id(int(get_jwt_identity()))
        new_house = HouseModel(**data,owner=current_user)


        # try:
        new_house.save_to_db()
        print(new_house.json())
        return new_house.json()
        # except:
            # return {"message": "An error occurred inserting the item."}, 500

        # item = ItemModel(name, **data)

        # try:
        #     item.save_to_db()
        # except:
        #     return {"message": "An error occurred inserting the item."}, 500

        # return item.json(), 201


class HousesWithInRadius(Resource):
    def get(self, distance, lon, lat):
        print(distance,lon,lat)
        housesWithInRadius = HouseModel.housesWithInRadius(distance,lon,lat)
        print(housesWithInRadius)
        # return {'houses': list(map(lambda x: x.json(), HouseModel.query.all()))}
        