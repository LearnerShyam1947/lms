from flask_restful import Api
from .BookRequestHandler import *
from .UserRequestHandler import UserRequestHandler, SingleUserHandler
    
api = Api()

api.add_resource(BooksRequestHandler, "/book-api/<id>")
api.add_resource(CategoryRequestHandler, '/category-api/<id>')
api.add_resource(BorrowBookRequestHandler, '/barrow-api/<id>')
api.add_resource(UserRequestHandler, '/user-api/<id>')
api.add_resource(SingleUserHandler, '/user-api/verify/<id>')