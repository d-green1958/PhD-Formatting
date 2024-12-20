import PyhD.matplotlib as phd_plot
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 10, 100)
y = np.random.rand(100)

# phd_plot.apply_style()
fig, axs = phd_plot.landscape_fig(
    title="Test", x_label="time", x_arrs=[x, x, x, x], y_arrs=[y, y + 1, y + 2, y + 3], legend=True
)

import os
phd_plot.save_fig(fig, os.getcwd(), "test")

plt.show()
