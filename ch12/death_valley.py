import csv
from datetime import datetime
from matplotlib import pyplot as plt

with open('csv/death_valley_2014.csv') as f:
    text = csv.reader(f)
    header_row = next(text)
    dates, highs, lows = [], [], []
    for row in text:
        try:
            current_date = datetime.strptime(row[0], "%Y-%m-%d")
            high = int(row[1])
            low = int(row[3])
        except ValueError:
            print(current_date, 'missing date')

        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)

fig = plt.figure(dpi=128, figsize=(10,6))
plt.plot(dates, highs, c='blue', alpha=0.5)
plt.plot(dates, lows, c='black', alpha=0.5)
plt.fill_between(dates, highs, lows,facecolor='red', alpha=0.1)

title = "Day high and low temperatures - 2014\nDeath Valley"
plt.title(title, fontproperties='Menlo', fontsize=20)
plt.xlabel('Time', fontsize=16, fontproperties='Menlo')
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize=20, fontproperties='Menlo')
plt.tick_params(axis='both', which='major', labelsize=16)
plt.savefig('', dpi=800)
plt.render_to_file('death_valley.png', dpi=800)
plt.show()