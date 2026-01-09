# Alarm Clock
# Plays an alarm sound at a specific time (HH:MM)

import time
from datetime import datetime


def alarm_clock(alarm_time):
    print(f"Alarm set for {alarm_time}")

    while True:
        current_time = datetime.now().strftime("%H:%M")

        if current_time == alarm_time:
            print("\n⏰ ALARM! Time to wake up! ⏰")
            break

        time.sleep(10)  # check every 10 seconds


def main():
    alarm_time = input("Enter alarm time (HH:MM): ")

    try:
        datetime.strptime(alarm_time, "%H:%M")
        alarm_clock(alarm_time)
    except ValueError:
        print("Invalid time format. Please use HH:MM (24-hour format).")


if __name__ == "__main__":
    main()
