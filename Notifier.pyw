import datetime
import time
import schedule
import random
import requests
from winotify import Notification

# List of possible notification titles and messages
title_list = ["Thundering Triumphs", "Racing Reimagined", "Velocity Unleashed", "Last Lap Legends", "Chasing the Checkered", "Curves and Conquests", "Grit and Glory", "Podium Chronicles", "Speedscape Chronicles", "Pinnacle Pursuit"]
msg_list = ["The Unpredictable Victory of the Latest Formula 1 Race", "A Recap of the Latest Thrills in Formula 1", "Unraveling the Latest Formula 1 Racing Spectacle", "Heroes and Surprises from the Latest Formula 1 Race", "Drama and Triumph in the Latest Formula 1 Showdown", "The Latest Formula 1 Race's Unforgettable Moments", "Latest Formula 1 Race Chronicles of Courage and Strategy", "A Tale of Victory and Redemption in the Latest Formula 1 Race", "Recounting the Latest Formula 1 Race's High-Speed Drama", "The Latest Formula 1 Race's Search for Racing Excellence"]

race_index = 12

def send_notification(race_index) :

    # Get the data for the next race from the API
    url = "http://ergast.com/api/f1/2023.json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        race = data['MRData']['RaceTable']['Races'][race_index]
    else:
        print(f'Error: {response.status_code}')
    
    # Analyse the scheduled time for the next race
    time_str = race['time'].rstrip('Z')
    scheduled_time = datetime.datetime.strptime(race['date'] + ' ' + time_str, '%Y-%m-%d %H:%M:%S')
    scheduled_time += datetime.timedelta(hours=2)

    # Create the notification with a random title and message
    toast = Notification(app_id="F1 Result lastet Race",
    title = random.choice(title_list),
    msg = random.choice(msg_list),
    duration = "long",
    icon = r"F:\f1.png",
    )

    # Add an action to the notification that launches a program when clicked
    toast.add_actions(label="Click Here!", launch="F:\99_CDE\Python/Program.py")
    toast.show()

    race_index += 1

    # Schedule the next notification for the next race and reset for the next season
    if race_index < 21:
        schedule.every().race['date'].at(scheduled_time).do(send_notification, race_index=race_index)
    else:
        race_index = 0
    return race_index

while True:
    schedule.run_pending()
    time.sleep(1)