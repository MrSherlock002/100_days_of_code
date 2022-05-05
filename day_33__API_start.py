##########################################################################
##
##  Prasad R. Bhosale
##  Thurssday (5/05/2022)
##  day_33__API_start
##
##########################################################################

import requests

response = requests.get("http://api.open-notify.org/iss-now.json")
print(response)
# if response.status_code !=200:
#     raise Exception("Bad response from ISS ")

if response.status_code ==404:
    raise Exception("That resource does not exist.")
elif response.status_code == 401:
    raise Exception("You are not authorised to access this data.")

response.raise_for_status()

data = response.json()
longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude,latitude)

print(f"Data :{data}\n Longitude {longitude}\n Latitude{latitude}")
print(iss_position)
# HTTP Response code
"""
1XX : Hold On
2XX : Here you go
3XX : Go Away
4XX : You Screwed Up
5XX : I Screwed Up

"""
