#15-8
import pygal
from die import Die

die_0 = Die()
die_1 = Die()
die_2 = Die()

results = [die_0.roll() + die_1.roll() + die_2.roll()
           for roll_num in range(50000)]

max_result = die_0.num_sides + die_1.num_sides + die_2.num_sides
frequencies = [results.count(value) for value in range(3, max_result + 1)]

hist = pygal.Bar()

hist.title = "Results of rolling three D6 dice 50,000 times."
hist.x_labels = [str(x) for x in range(3, max_result + 1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D6 + D6', frequencies)
hist.render_to_file('die_visual_3d6.svg')

