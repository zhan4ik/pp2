import datetime

date1 = datetime.datetime(2023, 3, 3, 12, 0, 0)
date2 = datetime.datetime(2023, 3, 4, 12, 0, 0)

x = (date2 - date1).total_seconds()

print(x)