import time
import schedule
from winotify import Notification

def send_notification() :
    toast = Notification(app_id="F1 Result lastet Race",
    title = "Who win the race ?",
    msg = "A surprise it's possible ?",
    duration = "long",
    icon = r"F:\f1.png",
    )

    toast.add_actions(label="Click Here!", launch="F:\99_CDE\Python/Program.py")
    toast.show()

schedule.every().monday.at("13:32").do(send_notification)

while True:
    schedule.run_pending()
    time.sleep(1)