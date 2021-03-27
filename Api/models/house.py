from db import db
from geoalchemy2 import Geometry
from geoalchemy2.shape import to_shape
from sqlalchemy import func
# from sqlalchemy import funct
from sqlalchemy import cast
from geoalchemy2 import Geography


class HouseModel(db.Model):
    __tablename__ = 'houses'

    _id = db.Column(db.Integer, primary_key=True)
    location_word = db.Column(db.String(80))
    coordinates = db.Column(Geometry(geometry_type='POINT'))
    number_of_bedrooms = db.Column(db.Integer)
    # image_cover = db.Column(db.String(200))
    rent_amount_per_month = db.Column(db.Float(precision=2))
    area_in_square_meter = db.Column(db.Float(precision=2))
    description = db.Column(db.String(200))


    owner_id = db.Column(db.Integer, db.ForeignKey('users._id'))
    # user = db.relationship('UserModel')

    # def __init__(self, name, price, store_id):
    #     self.name = name
    #     self.price = price
    #     self.store_id = store_id
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()
    
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
        
    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(_id=id).first()


    @classmethod
    def housesWithInRadius(cls, distance, lon, lat):
        DISTANCE = distance #100 meters
        houseWithIn = db.session.execute("select * from houses where ST_DWithin(houses.coordinates,ST_MakePoint(9.0436513,38.7590634)::geography,1000);")
        # houseWithIn = db.session.query(cls).filter(func.ST_DWithin(cls.coordinates, cast(func.ST_SetSRID(func.ST_MakePoint(float(lon), float(lat)), 1609), Geography), DISTANCE)).all()
        housesWithInRadius = []
        for house in houseWithIn:
            
            print(house)
        # print(houseWithIn)
        return houseWithIn




    def json(self):
        return {
            '_id': self._id,
            'location_word': self.location_word, 
            'coordinates':{'lon':to_shape(self.coordinates).x, 'lat':to_shape(self.coordinates).y}, 
            'number_of_bedrooms': self.number_of_bedrooms,
            'rent_amount_per_month': self.rent_amount_per_month,
            'area_in_square_meter':self.area_in_square_meter,
            'description': self.description
         }
