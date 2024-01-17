import requests


drivers = 'https://ergast.com/api/f1/2023/driverStandings.json'

r = requests.get(drivers)

data = r.json()

print(data)



