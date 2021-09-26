import time
import plyer
from plyer import notification

if __name__ == "__main__":
    while True:
        notification.notify(
            title="Drink Water",
            app_name="Water Notifier",
            message="Please drink water, you have to drink water to stay healthy and to live. Your goal is to drink 3.7 litres of water in a day.",
            timeout=10,
            app_icon="./icon.ico",
            toast=True,
            ticker="try",
        )
        time.sleep(60*60)
