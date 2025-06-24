import time
from plyer import notification

while True:
    print("Please sip some water!")
    notification.notify(title="Drink Water",message="Please sip some water!")
    time.sleep(60*60)
