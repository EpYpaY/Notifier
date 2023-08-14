import requests
import json
import msvcrt

url = 'http://ergast.com/api/f1/current/last/results.json'

response = requests.get(url)

if response.status_code == 200:
    data = json.loads(response.text)
    
    for i in range(20):
        driver = data['MRData']['RaceTable']['Races'][0]['Results'][i]['Driver']
        givenName = driver['givenName']
        familyName = driver['familyName']
        position = int(data['MRData']['RaceTable']['Races'][0]['Results'][i]['position'])
        print(f'{givenName} {familyName} finish in {position}{"th" if position > 3 else ["st", "nd", "rd"][position-1]} position')

else:
    print('Error: {response.status_code}')

print("Double press enter to exit...")
msvcrt.getch()