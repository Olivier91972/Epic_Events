# EPIC EVENTS CRM

## Objectives

This project is a Customer Relationship Management (*CRM*) API designed for _Epic Events_, 
an events management company.

The RESTful API is implemented with a secured database built with Django ORM and PostgreSQL.

## Installation

Launch the console, go to the folder of your choice and clone this repository:
```
git clone https://github.com/Olivier91972/Epic_Events.git
```
Go to the API folder and create a new virtual environment:
```
python -m venv env
```
Then activate it:

Windows:
```
env\scripts\activate.bat
```
Linux:
```
source env/bin/activate
```
Then install the required packages:
```
pip install -r requirements.txt
```

## Create and link PostgreSQL database

Install [PostgreSQL](https://www.postgresql.org/download/).
Follow the [documentation](https://www.postgresql.org) to run the server.

Create a new PostgreSQL database with SQL shell (psql) : ```CREATE DATABASE your_db_name;```

In ```./epicEvents/settings.py``` set your PostgreSQL database information.

    NAME = your_db_name
    USER = your_db_user
    PASSWORD = your_db_password

## Migrate the database

To migrate, run ```python manage.py migrate```. The 3 user teams (admin, sales, support) are 
automatically created; to learn more about user teams and their permissions, 

## Create a superuser

Run ```python manage.py createsuperuser```.

## Usage

Run the server with ```python manage.py runserver```.

## Postman

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/28927944/2s9YR57aRo)


<h3>Documentation and usage details for API endpoints</h3>
	<p>
		Once the server is launched, read the following document before making your first requests to the API.<br>
	</p>
	<table>
		<tr>
			<th>API endpoint</th>
			<th>HTTP method</th>
			<th>URI
                <br>Curl
            </th>
		</tr>
		<tr>
			<td>Login
            </td>
			<td>POST</td>
			<td>http://127.0.0.1:8000/api/login/ 
                <br>Body / form-data:
                <br>'username=""'
                <br>'password=""'
                <br>
                <br> * A successful registration request returns an access and refresh token in the response.
            </td>
		</tr>
        <tr>
			<td>Refresh 
                <br>(Token refresh)
            </td>
			<td>POST</td>
			<td>http://127.0.0.1:8000/api/token/refresh/ 
            <br>Body / form-data:
            <br>'refresh="Token refresh"'
            </td>
		</tr>
		<tr>
			<td>Get all users</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/users/
				<br>
				<br>* Only administrator users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get one user</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/users/{user_id}/
				<br>
				<br>* Only administrator users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Add new user</td>
			<td>POST</td>
			<td>http://127.0.0.1:8000/api/users/
			<br>Body / form-data:
                <br>'username=""'
                <br>'password=""'
				<br>
                <br>'first_name=""'
                <br>'last_name=""'
                <br>'email=""'
                <br>'is_staff=""'
                <br>'is_active=""'
                <br>'groups=""'
                <br>
				<br>* Only administrator users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Update user</td>
			<td>PUT</td>
			<td>http://127.0.0.1:8000/api/users/{user_id}/
                <br>Body / form-data:
                <br>'username=""'
                <br>'password=""'
				<br>
                <br>'first_name=""'
                <br>'last_name=""'
                <br>'email=""'
                <br>'is_staff=""'
                <br>'is_active=""'
                <br>'groups=""'
                <br>
				<br>* Only administrator users can access this endpoint.
            </td>
		</tr>
		<tr>
			<td>Delete user</td>
			<td>DELETE</td>
			<td>http://127.0.0.1:8000/api/users/{user_id}/
				<br>
				<br>* Only Superuser users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get all clients</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/clients/
				<br>
				<br>* All authenticated users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get one client</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/clients/{client_id}/
				<br>
				<br>* All authenticated users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Add new client</td>
			<td>POST</td>
			<td>http://127.0.0.1:8000/api/clients/
				<br>Body / form-data:
                <br>'first_name=""'
                <br>'last_name=""'
                <br>'email=""'
                <br>'phone=""'
                <br>'mobile=""'
                <br>'company_name=""'
				<br>'sales_contact=""'
				<br>
				<br>* Only admin or sales team users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Update client</td>
			<td>PUT</td>
			<td>http://127.0.0.1:8000/api/clients/{client_id}/
				<br>Body / form-data:
                <br>'first_name=""'
                <br>'last_name=""'
                <br>'email=""'
                <br>'phone=""'
                <br>'mobile=""'
                <br>'company_name=""'
				<br>'sales_contact=""'
				<br>
				<br>* Only admin or sales team users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Delete client</td>
			<td>DELETE</td>
			<td>http://127.0.0.1:8000/api/clients/{client_id}/
			<br>
			<br>* Only admin users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get all contracts</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/contracts/
				<br>
				<br>* All authenticated users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get one contract</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/contracts/{contract_id}/
				<br>
				<br>* All authenticated users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Add new contract</td>
			<td>POST</td>
			<td>http://127.0.0.1:8000/api/contracts/
                <br>Body / form-data:
                <br>'client=""'
                <br>'sales_contact=""'
                <br>'amount=""' 
                <br>'payment_due=""'
				<br>
                <br>'status=""'
				<br>
				<br>* Only admin or sales team users can access this endpoint.
            </td>
		</tr>
		<tr>
			<td>Update contract</td>
			<td>PUT</td>
			<td>http://127.0.0.1:8000/api/contracts/{contract_id}/
                <br>Body / form-data:
                <br>'client=""'
                <br>'sales_contact=""'
                <br>'amount=""' 
                <br>'payment_due=""'
				<br>
                <br>'status=""'
				<br>
				<br>* Only admin or sales team users can access this endpoint.
            </td>
		</tr>
		<tr>
			<td>Delete contract</td>
			<td>DELETE</td>
			<td>http://127.0.0.1:8000/api/contracts/{contract_id}/
			<br>
			<br>* Only admin users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get all events</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/events/
				<br>
				<br>* All authenticated users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Get one event</td>
			<td>GET</td>
			<td>http://127.0.0.1:8000/api/events/{event_id}/
				<br>
				<br>* All authenticated users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Add new event</td>
			<td>POST</td>
			<td>http://127.0.0.1:8000/api/events/
				<br>Body / form-data:
                <br>'client=""'
                <br>'support_contact=""'
                <br>'event_status=""' 
                <br>'attendees=""'
				<br>'event_date=""'
                <br>'note=""'
				<br>
				<br>'contract=""'
				<br>
				<br>* Only admin or sales team users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Update event</td>
			<td>PUT</td>
			<td>http://127.0.0.1:8000/api/events/{event_id}/
				<br>Body / form-data:
                <br>'client=""'
                <br>'support_contact=""'
                <br>'event_status=""' 
                <br>'attendees=""'
				<br>'event_date=""'
                <br>'note=""'
				<br>
				<br>'contract=""'
				<br>
				<br>* Only admin or support team users can access this endpoint.
			</td>
		</tr>
		<tr>
			<td>Delete event</td>
			<td>DELETE</td>
			<td>http://127.0.0.1:8000/api/events/{event_id}/
				<br>
				<br>* Only admin users can access this endpoint.
			</td>
		</tr>
	</table>

