
parcels = []

class Parcel():
	def __init__(self):
		self.db = parcels

	""" Create a parcel delivery order """
	def create_parcel(self, sender_name, recipient_name, email, destination, weight, status, userId):
		parcel = {
					"sender_name": sender_name,
					"recipient_name": recipient_name,
					"email": email,
					"destination": destination,
					"weight": weight,
					"status": status,
					"parcelId": len(self.db) + 1,
					"userId": userId
		}
		self.db.append(parcel)
		# return parcel, 201

	""" Fetch a specific parcel delivery order when provided an existing order id"""
	def get_parcel(self, parcelId):
		p = [parcel for parcel in self.db if parcelId == parcel['parcelId']]
		if p:
			return {'Parcel': p[0]}, 200
		else:
			return {'Error': 'No parcel delivery order matches the id {}'.format(parcelId)}, 404

	""" Fetch all parcel delivery orders """
	def get_all_parcels(self):
		return {'Parcels': self.db}, 200

	""" Fetch all parcel delivery orders per specific user """
	def get_all_parcels_per_user(self, user_id):
		for parcel in self.db:
			if parcel['userId'] == userId:
				return {'Parcels by user id {}'.format(userId), parcel}, 200
			else:
				return {'No delivery order by user id {}'.format(userId)}, 404

	""" Cancel specific parcel delivery order """	
	def cancel_parcel_order(self, parcelId):
 		p = [parcel for parcel in self.db if parcelId == parcel['parcelId']]
 		if p:
 			self.db.remove(p)
 			return {'Success': 'Delivery order successfully cancelled'}, 200
 		else:
 			return {'Error': 'Parcel delivery order {}'.format(parcelId) + ' does not exist'}, 404