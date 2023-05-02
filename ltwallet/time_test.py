import time
t = time.localtime(time.time())
hour = t.tm_hour
mint = t.tm_min
sec = t.tm_sec
current_time = (f"{hour}:{mint}:{sec}")
print(current_time)