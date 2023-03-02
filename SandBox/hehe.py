from datetime import timedelta

t1 = timedelta(hours=7, minutes=36)
t2 = timedelta(hours=11, minutes=32)
t3 = timedelta(hours=13, minutes=7)
t4 = timedelta(hours=21, minutes=0)

arrival = t2 - t1
lunch = (t3 - t2 - timedelta(hours=1))
departure = t4 - t3

print(arrival, lunch, departure)