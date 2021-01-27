import psutil


battery = psutil.sensors_battery()
plugged = battery.power_plugged
percent = str(battery.percent)

plugged = "Plugged In" if plugged else "Not Plugged In"

print(percent+'%')
print(plugged)