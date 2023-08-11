import datetime
import time
import requests
from plyer import notification

f1data = None
try:
    f1data = requests.get("http://ergast.com/api/f1/current/last/results")
except:
    print("Error: Try again later")