import unittest
import json
from ...app import create_app

class TestParcel(unittest.TestCase):
	def setUP(self):
		self.app = create_app()
		self.client = self.app.test_client()
		self.app_context = self.app

		self.order = {
				"sender_name": "Andrew J",
				"recipient_name": "John D",
				"email": "john@gmail.com", 
				"destination": "Mombasa",
				"weight": 3,
				"status": "Transit",
				"userId": 2,
				"parcelId": 1
		}

		self.user = {

				"userId": 2,
            	"email": "andrewj@gmail.com",
            	"firstName": "J",
            	"lastName": "Andrew"
		}

	def test_post(self):
		response = self.client.post('/api/v1/parcel', data = json.dumps(self.order), content_type = 'application/json')
		result = json.loads(respose.data.decode())
		assert result == {"messge": "Parcel order successfully created"},201

		