from flask_restful import Resource, reqparse
from flask import Flask
from flask import request
from models.user import UserModel
from email_validator import validate_email, EmailNotValidError
from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from itsdangerous import URLSafeTimedSerializer, SignatureExpired
from mail import mail
from flask_mail import Message
# mail = Mail(current_app)

s = URLSafeTimedSerializer('Thisisasecret!')

class UserRegister(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help="user must have user name.")
    parser.add_argument('password', type=str, required=True, help="user must have password.")
    parser.add_argument('password_confirm', type=str, required=True, help="user must have passwordConfirm.")
    parser.add_argument('email', type=str, required=True, help="user must have email.")
    parser.add_argument('phone_number', type=str, required=True, help="user must have phone number.")
    

    def post(self):
        data = UserRegister.parser.parse_args()
        if data['password'] != data['password_confirm']:
            return {
                "status": "failed",
                "message": "password and password_confirm are not the same"
            },401

        del data['password_confirm']


        #  save him to database and set confirmed to false
        try:
            valid = validate_email(data['email'])

            # email = valid.data['email']
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            return {"message": str(e)}, 400
        # if UserModel.find_by_email(data['email']):
        #     return {"message": "A user with that email already exists"}, 400

        # send email verification here

        user = UserModel(**data)
        user.save_to_db()

        token = s.dumps(data['email'], salt='email-confirm')
        recipient = data['email']

        url = request.host_url + "api/v1/users/confirm_email/"+token
        # send him the adress including the token
        # 
        msg = Message('Confirm Email', sender='biruk@kassaw', recipients=[data['email']])
        msg.body = url
        msg.html = f"<p>Welcome! Thanks for signing up. Please follow this link to activate your account:</p><p><a href=\"{url}\">{url}</a></p><br><p>kiray bet</p>"
        mail.send(msg)
        return {"message": "confirmation email sent to your email adress go to your email to finish your registration","url": url}, 201


class ConfirmEmail(Resource):
    def get(self, token):
        # validate the token change the confirmed to true then send him jwt if it is correct
        try:
            email = s.loads(
                token,
                salt='email-confirm',
                max_age=3600
            )
        except:
            return {
                    "status": "failed",
                    "message":"The confirmation link is invalid or has expired."
                    }, 401

        user = UserModel.find_by_email(email)
        if user.confirmed:
            return {
                    "status": "sucess",
                    "message":"your account has been activated log in."
                    }
        user.confirmed = True
        user.save_to_db()

        access_token = create_access_token(identity=user._id)
        return {
                "status": "sucess",
                "message": "account activated sucessfully",
                "data": {
                    "jwt": access_token
                }
            }

class UserLogin(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help="user must have email to login..")
    parser.add_argument('password', type=str, required=True, help="user must have password to login.")
    def post(self):
        data = UserLogin.parser.parse_args()
        email = data["email"]
        password = data["password"]

        print(email+" "+password)
        user = UserModel.find_by_email(email)

        if user and user.confirmed == False:
            return {
                "status": "failed",
                "message": "confirm your email first"
            }, 401

        if user  and user.password == password:
            access_token = create_access_token(identity=user._id)
            return {
                "status": "sucess",
                "data": {
                    "jwt": access_token
                }
            }

        return {"message": "Invalid email or password"}, 400

class ForgotPassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help="user must have account email to reset password.")

    def post(self):
        data = ForgotPassword.parser.parse_args()
        email = data["email"]
        user = UserModel.find_by_email(email)
        if user is None:
            return {"message": "no user with that email adress"}, 400

        token = s.dumps(data['email'], salt='email-confirm')
        recipient = data['email']

        url = request.host_url + "api/v1/users/resetPassword/"+token
        # send him the adress including the token
        # 
        msg = Message('Confirm Email', sender='biruk@kassaw', recipients=[data['email']])
        msg.body = url
        msg.html = f"<p>send a put request with your new passsword to the following url:</p><p><a href=\"{url}\">{url}</a></p><br><p>kiray bet</p>"
        mail.send(msg)
        return {
                    "status": "sucess",
                    "message": "Token sent to your email account "
        }
        # generate a random token and sent it to the email


class ResetPassword(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('password', type=str, required=True, help="user must have the new password to reset password.")
    parser.add_argument('password_confirm', type=str, required=True, help="user must have passwordConfirm to reset password.")

    def put(self,token):
        data = ResetPassword.parser.parse_args()
        if data['password'] != data['password_confirm']:
            return {
                "status": "failed",
                "message": "password and password_confirm are not the same"
            },401

        del data['password_confirm']
        print(data["password"])

        try:
            email = s.loads(
                token,
                salt='email-confirm',
                max_age=3600
            )
        except:
            return {
                    "status": "failed",
                    "message":"The confirmation link is invalid or has expired."
                    }, 401


        user = UserModel.find_by_email(email)
        user.password = data["password"]
        user.save_to_db()

        return {
                    "status": "sucess",
                    "message":"password changed sucessfully"
                    }, 201
        