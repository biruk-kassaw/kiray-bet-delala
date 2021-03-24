from flask import Flask
from flask_restful import Api
from sqlalchemy import event
# from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager
from resources.user import UserRegister, UserLogin, ConfirmEmail, ForgotPassword, ResetPassword
from resources.house import House, HouseList, HousesWithInRadius
# from resources.store import Store, StoreList
# from flask_mail import Mail, Message

app = Flask(__name__)

app.config['MAIL_SERVER']='smtp.mailtrap.io'
app.config['MAIL_PORT'] = 2525
app.config['MAIL_USERNAME'] = '05873cf083fae6'
app.config['MAIL_PASSWORD'] = '2a4b487d0b1ebd'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False

 
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config["JWT_ACCESS_TOKEN_EXPIRES"] = False
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://biruk:2356@localhost:5432/webproject"
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config["JWT_SECRET_KEY"] = "super-secret jwt key ;laskdjf"
app.config.from_pyfile('config.cfg')

app.secret_key = 'house_rent_project fa;lsdkjf;akj'
jwt = JWTManager(app)
api = Api(app)


@app.before_first_request
def create_tables():
    # db.engine.execute('create extension postgis') 
    db.create_all()



# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(StoreList, '/stores')

api.add_resource(House, '/api/v1/houses/<id>')
api.add_resource(HouseList, '/api/v1/houses')
api.add_resource(HousesWithInRadius, '/api/v1/houses/houses-within/<distance>/center/<lon>/<lat>')
api.add_resource(UserRegister, '/api/v1/users/register')
api.add_resource(UserLogin, '/api/v1/users/login')
api.add_resource(ConfirmEmail, '/api/v1/users/confirm_email/<token>')
api.add_resource(ForgotPassword, '/api/v1/users/forgotPassword')
api.add_resource(ResetPassword, '/api/v1/users/resetPassword/<token>')



if __name__ == '__main__':
    from db import db
    from mail import mail
    db.init_app(app)
    mail.init_app(app)

    app.run(port=5000, debug=True)
