#15-9
import pygal
from die import Die

die_0 = Die()
die_1 = Die()

results = [die_0.roll() * die_1.roll() for roll_num in range(50000)]

max_result = die_0.num_sides * die_1.num_sides
frequencies = [results.count(value) for value in range(1, max_result + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling two D6 50000 times."
hist.x_labels = [str(x) for x in range(1, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 * D6', frequencies)
hist.render_to_file('die_visual_d6d6.svg')
