import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
import redis

from moviepy.video.io.bindings import mplfig_to_npimage
import moviepy.editor as mpy

duration = 2
fig_mpl, ax = plt.subplots(1, figsize=(5, 3), facecolor='white')
xx = np.linspace(-2, 2, 200)
zz = lambda d: np.sinc(xx**2)+np.sin(xx+d)
ax.set_title("Elevation in y=0")
ax.set_ylim(-1.5, 2.5)
line, = ax.plot(xx, zz(0), lw=3)


def make_frame_mpl(t):
    line.set_ydata(zz(2*np.pi*t/duration))
    return mplfig_to_npimage(fig_mpl)
animation=mpy.VideoClip(make_frame_mpl, duration=duration)
animation.write_gif("sinc_mpl.gif", fps=20)
