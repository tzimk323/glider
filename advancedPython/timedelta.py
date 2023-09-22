from datetime import datetime, timedelta

current_time = datetime.now()
new_time = current_time + timedelta(minutes=60)

print("Current Time:", current_time)
print("New Time:", new_time)