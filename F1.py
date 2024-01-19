import requests
championship = '' #setting so below loop while requires break via correct user input

#Welcome message
print("--------------------------------------------------------------------------------------------------------------------")
print("Welcome, this program harnesses the Ergast Developer API to access data relating the Formula One world championship.")
print("This program supports requests from the first F1 season in 1950 to current day.")
print("Enter a year below to retrieve driver or constructor championship information.")
print()
print("NOTE: Constructors Championship was not awarded until 1958, Drivers Championship was awarded from 1950.")
print()

#while loop to return user to start
while True:
    print("Type 'exit' to quit, or")
    year = input("Enter year: ") #user input stored as year

    #sets year to lowercase to accept any case input from user for exit. break ends program.
    if year.lower() == 'exit':
        print("Exiting program...")
        break
    
    #convert year to integer and check its within data range, if not returns user to enter year again.
    if int(year) not in range(1950,2024):
        print(f"No data for {year}, please enter a year between 1950 and 2023 season.")
        continue
      
    championship = '' #setting so below loop while requires break via correct user input

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
            print()

            #extract data from json structure to dStandings, 0 index is for entire championship not rd1
            dStandings = data['MRData']['StandingsTable']['StandingsLists'][0]['DriverStandings']
            #loop through extracting data for each driver  
            for driverData in dStandings:       
                position = driverData['position']
                givenName = driverData['Driver']['givenName'] 
                familyName = driverData['Driver']['familyName']
                code = driverData['Driver'].get('code', '---') #set default value where data is missing
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

    #check if user selected constructors standings before 1958, if OK year runs GET request, else returns to enter year.
    elif championship =='2':
        if int(year) >= 1958:
            constructors = f'https://ergast.com/api/f1/{year}/constructorStandings.json'
            rc =requests.get(constructors)

            if rc.status_code == 200:
                data =rc.json()

                print(f"Retrieving {year} constructors standings...")
                print()

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
        else:
            #message if constructor championship selected for year before 1958
            print("The Constructors Championship was not awarded until 1958.")