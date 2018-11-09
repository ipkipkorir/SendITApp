from flask import Flask
from flask import request, make_response
from flask_restful import Resource, Api
#import models
from .models import Parcel

# app = Flask(__name__)
# api = Api(app)

# Creating parcel delivery order
class PostParcel(Resource, Parcel):
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
		return order

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

# Fetching specific user parcel delivery order
class GetSpecificUserOrders(Resource, Parcel):
	def __init__(self):
		self.parcel = Parcel()

	def get(self):
		user_order = self.parcel.get_all_parcels_per_user()
		return user_order


# Cancelling specific parcel delivery order
class RemoveSpecificParcel(Resource, Parcel):
	def __init__(self):
		self.parcel = Parcel()	

	def put(self, parcelId):
		cancel_order = self.parcel.cancel_parcel_order(parcelId)
		return cancel_order