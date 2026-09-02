import time
from plyer import notification

def water_reminder():
    while True:
        notification.notify(
            title='Water Reminder for Kanak',
            message='Time to drink water!',
            timeout=10
        )
        time.sleep(3600)  # Remind every hour
        #time.sleep(5)  # for testing purposes

water_reminder()
