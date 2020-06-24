#rw_visual
import matplotlib.pyplot as plt
from  random_walk import  RandomWalk

while True:
    rw = RandomWalk(5000)
    rw.fill_walk()
    point_numbers = list(range(rw.num_points))
    plt.plot(rw.x_values, rw.y_values, linewidth=1, c="#AFFFAE")
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    plt.show()
    keep_running = input("Make another walk? (yes/no):")
    if keep_running == 'no':
        break