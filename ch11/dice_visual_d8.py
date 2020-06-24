#15-7
import pygal
from die import Die

die_0 = Die(8)
die_1 = Die(8)

results = [die_0.roll() + die_1.roll() for roll_num in range(50000)]

max_results = die_0.num_sides + die_1.num_sides
frequencies = [results.count(value) for value in range(2, max_results + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D8 dice 50,000 times."
hist.x_labels = [str(x) for x in range(2, max_results + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D8 + D8', frequencies)
hist.render_to_file('die_visual_d8.svg')