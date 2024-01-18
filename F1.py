import requests
championship = '' #setting so below loop while requires break via correct user input

year = input("Enter the season year: ") #user input stored as year

#while loop to ensure user enters valid input
while championship != '1' or championship != '2':       
    championship = input(f"Enter 1 for {year} drivers standings, or 2 for constructors standings: ")
    if championship == '1' or championship == '2':
        break

if championship == '1': 

    drivers = f'https://ergast.com/api/f1/{year}/driverStandings.json' #adds user inputted year to URL
    rd = requests.get(drivers)  #send GET request to API

    if rd.status_code == 200: #checks status code success, if error prints status code
        data = rd.json()  #store json data from request in data

        print(f"Retrieving {year} drivers championship standings...")

        #extract data from json structure to dStandings, 0 index is for entire championship not rd1
        dStandings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
        #loop through extracting data for each driver  
        for driverData in dStandings:       
            position = driverData['position']
            givenName = driverData['Driver']['givenName'] 
            familyName = driverData['Driver']['familyName']
            code = driverData['Driver']['code']
            points = driverData['points']
            wins = driverData['wins']
            team = driverData['Constructors'][0]['name'] #access constructors list
        
            #output data into cli, each driver seperated by empty line
            print(f"{position}. {code}. {givenName} {familyName}: {points} pts, {wins} wins. ")           
            print(f"{team}")
            print()

    else:
        #print status code if not 200 OK
        print(f"ERROR {rd.status_code}: Unable to retrieve data.")

else:
    #if user enters 2, GET request for constructors standings
    constructors = f'https://ergast.com/api/f1/{year}/constructorStandings.json'
    rc =requests.get(constructors)

    if rc.status_code == 200:
        data =rc.json()

        print(f"Retrieving {year} constructors standings...")

        #extract data to cStandings, loop through each constructor and extract data
        cStandings = data['MRData']['StandingsTable']['StandingsLists'][0]['ConstructorStandings']
        for constructorData in cStandings:
            position = constructorData['position']
            name = constructorData['Constructor']['name']
            points = constructorData['points']
            wins = constructorData['wins']

            #output data to terminal, each constructor seperated by empty line
            print(f'{position}. {name} - {points} pts, {wins} wins.')
            print()

    else:
        #if status not 200 OK, print status code
        print(f"ERROR {rc.status_code}: Unable to retrieve data.")