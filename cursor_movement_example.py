import matplotlib.pyplot as plt
from matplotlib.backend_bases import MouseButton
import numpy as np
import matplotlib.animation as animation
import time
import random

t = np.arange(0.0, 1.0, 0.01)
s = np.sin(2 * np.pi * t)
fig, ax = plt.subplots()
ax.plot(t, s)


def on_move(event):
    if event.inaxes:
        print(f'data coords {event.xdata} {event.ydata},',
              f'pixel coords {event.x} {event.y}')

binding_id = plt.connect('motion_notify_event', on_move)
plt.show()
