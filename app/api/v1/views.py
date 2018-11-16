from flask import Flask
from flask import request, make_response
from flask_restful import Resource, Api
from .models import Parcel, User

# Creating parcel delivery order
class PostParcel(Resource):
	def __init__(self):
		self.parcel = Parcel()

	def post(self):

		order = self.parcel.create_parcel(
					request.json['sender_name'],
					request.json['recipient_name'],
					request.json['email'], 
					request.json['destination'],
					request.json['weight'],
					request.json['status'],
					request.json['userId'])

		return {"Message": "Parcel order successfully created"}

# Fetching specific parcel delivery order
class GetSpecificParcel(Resource, Parcel):
	def __init__(self):
		self.parcel = Parcel()

	def get(self, parcelId):
		specific_parcel = self.parcel.get_parcel(parcelId)
		return specific_parcel


# Fetching all parcels delivery orders
class GetAllParcels(Resource, Parcel):
	def __init__(self):
		self.parcel = Parcel()

	def get(self):
		all_parcels = self.parcel.get_all_parcels()
		return all_parcels

""" Create user class"""
class CreateUser(Resource, User):
	def __init__(self):
		self.users = User()

	def post(self):
		user = self.users.create_user(
					request.json['firstName'],
					request.json['lastName'],
					request.json['email'])
		return user

# Fetching specific user parcel delivery order
class GetSpecificUserOrders(Resource, Parcel, User):
	def __init__(self):
		self.parcel = Parcel()

	def get(self, userId):
		user_order = self.parcel.get_all_parcels_per_user(userId)
		return user_order

# Get all users
class GetAllUsers(Resource, User):
	def __init__(self):
		self.users = User()

	def get(self):
		all_users = self.users.get_all_users()
		return all_users

# Cancelling specific parcel delivery order
class CancelSpecificParcel(Resource, Parcel):
	def __init__(self):
		self.parcel = Parcel()	

	def put(self, parcelId):
		cancel_order = self.parcel.cancel_parcel_order(parcelId)
		return cancel_order