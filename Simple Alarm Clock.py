import time
alarm_time = input("Enter alarm time (hh:mm:ss): ")

while True:
    current_time = time.strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake Up!")
        break 