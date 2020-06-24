import csv
from datetime import datetime
from matplotlib import pyplot as plt
filename = 'csv/sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    line = next(reader)
    clouds, dates = [], []
    for row in reader:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            cloud = row[-3]
        except ValueError:
            print(row[0], 'missing date')
        else:
            clouds.append(cloud)
            dates.append(current_date)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, clouds, c='blue', alpha=0.1)
plt.title("Daily CloudCover -2014\nSitka", fontsize=24)
plt.xlabel("Time, fontsize=16")
plt.ylabel("CloudCover", fontsize=16)
fig.autofmt_xdate()
plt.show()