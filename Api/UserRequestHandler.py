from flask import request, render_template
from flask_restful import Resource, abort
from flask_mail import Message
from app import db, mail, app
from models import *
import threading

class UserRequestHandler(Resource):
    def get(self, id):
        user = User.query.filter_by(id = id).first()
        type = request.args.get('type')
        print(type)

        if type:
            if user:
                user.isAdmin = type
                if type == 1:
                    user.isVerified = 1

                db.session.commit()

                return {
                    'status' : 'success',
                    'code' : 200,
                }

            else:
                abort(404)

        else:
            abort(404)


    def delete(self, id):
        user = User.query.filter_by(id = id).first()

        if user:
            db.session.delete(user)
            db.session.commit()

            return {
                'status' : 'success',
                'code' : 200,
            }
        
        else:
            abort(404)

class SingleUserHandler(Resource):
        def get(self, id):
            print('I am here')
            user = User.query.filter_by(id = id).first()
            request_type = request.args.get('type')

            if request_type:
                if user:

                    user.isVerified = request_type

                    msg = Message('Account verification status', recipients=[user.email, ], sender='vitap.library@gmail.com')

                    msg.html = render_template('email/verified.html', user=user, request_type=request_type)

                    mail.send(msg)
                    
                    db.session.commit()

                    return {
                        'status' : 'success',
                        'code' : 200,
                    }

                else:
                    abort(404)

            else:
                abort(404)

def send_verified_mail(user):
    with app.app_context():
        print('started..........')
        # print('I am here : ', user)

        

        print("Send successfully.........")
