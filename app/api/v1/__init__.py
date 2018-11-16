from flask import Blueprint
from flask_restful import Api, Resource
from .views import GetAllParcels, GetSpecificParcel, CancelSpecificParcel, PostParcel, GetSpecificUserOrders, CreateUser, GetAllUsers

version1 = Blueprint('apiv1', __name__, url_prefix='/api/v1')
api = Api(version1)

"""EndPoint routes"""
api.add_resource(PostParcel, '/parcels')
api.add_resource(GetSpecificParcel, '/parcels/<int:parcelId>')
api.add_resource(CancelSpecificParcel, '/parcels/<int:parcelId>/cancel')
api.add_resource(GetAllParcels, '/parcels')
api.add_resource(GetSpecificUserOrders, '/users/<int:userId>/parcel')

# Create user
api.add_resource(CreateUser, '/users')
api.add_resource(GetAllUsers, '/users')
