import requests

year = input("Enter the season year: ")

drivers = f'https://ergast.com/api/f1/{year}/driverStandings.json' #adds user inputted year to URL
r = requests.get(drivers)   #send GET request to API URL defined above as 'drivers'

if r.status_code == 200:       #checks status code success, if error prints status code
    data = r.json()

    dStandings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings'] #extracting data, index set to 0 for whole season 
    for driverData in dStandings:       #loop through each driver record storing below variables
        position = driverData['position']
        givenName = driverData['Driver']['givenName'] 
        familyName = driverData['Driver']['familyName']
        code = driverData['Driver']['code']
        points = driverData['points']
        
        print(f"Pos: {position}")           #prints information for each driver with an empty line sperating them
        print(f"Driver: {givenName} {familyName} {code}")
        print(f"Points: {points}")
        print()

else:
    print(f"ERROR {r.status_code}: Unable to retrieve data.")


