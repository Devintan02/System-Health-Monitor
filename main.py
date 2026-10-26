import psutil

print(f"CPU usage: {psutil.cpu_percent(interval=1)}%")
print(f"Memory usage: {psutil.virtual_memory().percent}%")
print(f"Disk usage: {psutil.disk_usage('/').percent}%")