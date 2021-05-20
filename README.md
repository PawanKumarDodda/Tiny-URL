# Tiny-URL
Shortening the URl
Installation Set Up
-------------------
Install the Python Vesion more than 3.5
Install the django version 3.0
Install the django rest framework 
Install the postman

Commands to execute 
--------------------
To run the server : python manage.py runserver
To make migrations : python manage.py makemigrate
To migrate : python manage.py migrate
To create super user : python manage.py createsuperuser

Urls used in project :
----------------------
http://127.0.0.1:8000 ---> shows all the urls used in the project
http://127.0.0.1:8000/test ---> shows the testing page to ensure our application is working fine or not
http://127.0.0.1:8000/demo --->open our api

Business Logic:
---------------
The motive of this project is to shorten the URLS 
Used Class based API View for GET and POST Methods
First Scenario 
--------------
To store the shhortcode for the url in the Database
add the url and shortcode in the request body and add the request as POST
Note: shortcode should be of length 6 and it shoulf be alpha numeric
if url and shortcode code satisfies the condition will return shortcode as response and 201 as success status code
if url is not present wil return response as URL not present as present and 400 as  error status code
if shortcode is already exist in database will return respomse as shortcode already in use and 409 as status code
if short does not satisfies the condition will return respose as Invalid Shortcode and 412 as status code

Second Scenario
---------------
add the get request for the url
in request body we have to give only shortcode as parameter
the motive of the scenario is to check wheather short code is exists or not 
if success return status code as 302 and response as url
else return 404 as staus code and response as Shortcode Not Found.
