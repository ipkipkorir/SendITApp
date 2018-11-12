SendIT

Overview
SendIT is a courier service that helps users deliver parcels to different destinations. SendIT provides courier quotes based on weight categories.

Features
Users can create an account and log in.
Users can create a parcel delivery order.
Users can change the destination of a parcel delivery order.
Users can cancel a parcel delivery order.
Users can see the details of a delivery order.
Admin can change the status and present location of a parcel delivery order.

How to run the application
- Clone the repository link: https://github.com/ipkipkorir/SendITApp.git 
- Install python 3 on your computer
- Install and activate virtual environment on your local project directory
- Install flask
- Install flask restful
- Install postman
- Do flask run on the activated virtual environment
- Test on Postman the endpoint given below


Working API Endpoints:

GET /parcels
Fetch all parcel delivery orders

GET /parcels/<parcelId> 
Fetch a specific parcel delivery order

GET /users/<userId>/parcels
Fetch all parcel delivery orders by a specific user

POST /parcels
Create a parcel delivery order

Non-working Endpoint
PUT /parcels/<parcelId>/cancel
Cancel the specific parcel delivery order
