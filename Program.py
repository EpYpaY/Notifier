import requests
import msvcrt
import colorama
from tabulate import tabulate
from colorama import Fore, Style

colorama.init(True)

print(f"{Fore.RED}" +"""
______                ______                _ _   
| ___ \               | ___ \              | | |  
| |_/ /__ _  ___ ___  | |_/ /___  ___ _   _| | |_ 
|    // _` |/ __/ _ \ |    // _ \/ __| | | | | __|
| |\ \ (_| | (_|  __/ | |\ \  __/\__ \ |_| | | |_ 
\_| \_\__,_|\___\___| \_| \_\___||___/\__,_|_|\__|
                                                  
""" + f"{Style.RESET_ALL}")

url = 'http://ergast.com/api/f1/current/last/results.json'

response = requests.get(url)
if response.status_code == 200:
    data = response.json()

    init_race = data['MRData']['RaceTable']['Races'][0]
    RaceName = init_race['raceName']
    Locality = init_race['Circuit']['Location']['locality']
    print(f'Today event was {RaceName} at {Locality}!\n')

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
        if position == 1:
            results.append([Fore.LIGHTYELLOW_EX + str(position), number, f'{givenName} {familyName}', constructor, laps, time, pts ])
        elif position == 2:
            results.append([Fore.LIGHTCYAN_EX + str(position), number, f'{givenName} {familyName}', constructor, laps, time, pts])
        elif position == 3:
            results.append([Fore.LIGHTRED_EX + str(position), number, f'{givenName} {familyName}', constructor, laps, time, pts + Style.RESET_ALL])
        else:
            results.append([position, number, f'{givenName} {familyName}', constructor, laps, time, pts])

    print(tabulate(results, headers=['Position', 'Number', 'Drivers', 'Constructor', 'Laps', 'Time/Retired', 'Points'], numalign='center'))

else:
    print(f'Error: {response.status_code}')

print("\nDouble press enter to exit...")
msvcrt.getch()