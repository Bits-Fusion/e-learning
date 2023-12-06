import requests
import os
from rest_framework.response import Response
from getpass import getpass

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bits_fusion_labs.settings')


def getheaders(email, username, password):
	my_auth_end_point = 'http://localhost:8100/api_root/token/'
	auth_response = requests.post(
		my_auth_end_point, 
		json = {
			'email':email,
			'user_name':username,
			'password':password
		}
	)
	print(auth_response.json())
	return auth_response.json()['access'], auth_response.json()['refresh']


def refrashrequest(email, username, password):
	next_endpoint = f"http://localhost:9100/api_root/token/refresh/"
	header, refresh = makeheaders(email, username, password)
	new_request = requests.post(
		next_endpoint, 
		json = {
			'email':email,
			'user_name':username,
			'password':password,
			'refresh':refresh
		},
		headers = header
	)
	return new_request.json()


def makeheaders(email, username, password):
	access = getheaders(email, username, password)
	headers = {
	"Authorization": f"JWT {access[0]}"
	}
	return headers


def loginrequest(email, username, password, header):
	next_endpoint = f"http://localhost:9100/api_root/login/"
	new_request = requests.post(
		next_endpoint, 
		json = {
			'email':email,
			'user_name':username,
			'password':password, 
		},
		headers = header
	)
	return new_request.json()


def logoutrequest(email, username, password, header):
	next_endpoint = f"http://localhost:9100/api_root/logout/"
	new_request = requests.post(
		next_endpoint, 
		json = {
			'email':email,
			'user_name':username,
			'password':password, 
		},
		headers = header
	)
	return new_request.json()


def profile_changed(email, username, password, new_user_name, new_pass, header):
	next_endpoint = f"http://localhost:9100/api_root/profile/update/"
	new_request = requests.post(
		next_endpoint, 
		json = {
			'email':email,
			'user_name':new_user_name,
			'password':new_pass, 
		},
		headers = header
	)
	return new_request.json()

def get_profile(header):
	next_endpoint = f"http://localhost:8100/api_root/profile/root/"
	new_request = requests.get(
		next_endpoint, 
		headers = header
	)
	return new_request.json()

while True:
	user_name = input('User name: ')
	email = input('Email: ')
	password = getpass("Password: ")

	header = getheaders(email, user_name, password)
	new_head = {
	"Authorization": f"JWT {header[0]}"
	}

	response = loginrequest(email, user_name, password, new_head)
	print(response)
	# logout_response = logoutrequest(email, user_name, password, new_head)
	# print(logout_response)
	# user_name_1 = input('User name: ')
	# email_1 = input('Email: ')
	# password_1 = getpass("Password: ")
	# new_user_name = input('New User Name: ')
	# new_pass = getpass('New Pass: ')
	# change = profile_changed(
	# 			email_1,
	# 			user_name_1,
	# 			password_1,
	# 			new_user_name,
	# 			new_pass,
	# 			new_head
	# 		)
	# print(change)
	logout = get_profile(new_head)
	print(logout)

	