import requests

year = input("Enter the season year: ")

drivers = f'https://ergast.com/api/f1/{year}/driverStandings.json' #adds user inputted year to URL

r = requests.get(drivers)   #send GET request to API URL defined above as 'drivers'

data = r.json()

print(data)


