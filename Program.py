import requests
import json
import msvcrt
from tabulate import tabulate

print("""

______                ______                _ _   
| ___ \               | ___ \              | | |  
| |_/ /__ _  ___ ___  | |_/ /___  ___ _   _| | |_ 
|    // _` |/ __/ _ \ |    // _ \/ __| | | | | __|
| |\ \ (_| | (_|  __/ | |\ \  __/\__ \ |_| | | |_ 
\_| \_\__,_|\___\___| \_| \_\___||___/\__,_|_|\__|
                                                  
      
""")

url = 'http://ergast.com/api/f1/current/last/results.json'

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    
    RaceName = data['MRData']['RaceTable']['Races'][0]['raceName']
    Locality = data['MRData']['RaceTable']['Races'][0]['Circuit']['Location']['locality']
    print (f'Today event was {RaceName} at {Locality}!')
    print()

    results = []
    for i in range(20):
        init_pilot = data['MRData']['RaceTable']['Races'][0]['Results'][i]
        position = int(init_pilot['position'])
        number = init_pilot['number']
        driver = init_pilot['Driver']
        givenName = driver['givenName']
        familyName = driver['familyName']
        constructor = init_pilot['Constructor']['name']
        laps = init_pilot['laps']
        time = init_pilot.get('Time', {}).get('time', 'Retired')
        pts = init_pilot['points']
        results.append([position, number, f'{givenName} {familyName}', constructor, laps, time, pts])

    print(tabulate(results, headers=['Position', 'Number', 'Drivers', 'Constructor', 'Laps', 'Time/Retired', 'Points' ], numalign='center'))

else:
    print('Error: {response.status_code}')

print("Double press enter to exit...")
msvcrt.getch()