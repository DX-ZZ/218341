#15-6
from die import Die
import pygal

def num2char(x):
    return str(x)

die0 = Die()
die1 = Die()
results = []

for roll_num in range(1000):
    result = die0.roll() + die1.roll()
    results.append(result)

frequencies = []
max_result = die0.num_sides + die1.num_sides
for value in range(1, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

hist = pygal.Bar()
hist.title = "Results of rolling  D6 1000 times."
hist.x_labels = list(map(num2char, list(range(1, max_result + 1))))
print(hist.x_labels)
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6+D6', frequencies)
hist.render_to_file('die_visual_d6.svg')
