import matplotlib.pyplot as plt
from  ..style import apply_style
import numpy as np

def landscape_fig(x_label=None, y_label=None, title=None, x_arrs=None, y_arrs=None, label_arrs=None, legend=False, legend_title=None, tight_layout=False, suptitle=None):
    apply_style()
    figure = plt.figure(figsize=(6,4))
    axs = figure.gca()

    axs.set_title(title)
    axs.set_xlabel(x_label)
    axs.set_ylabel(y_label)
    
    if x_arrs is not None:
        if label_arrs is None:
            label_arrs = np.full(len(x_arrs), "")
        for ind,_ in enumerate(x_arrs):
            axs.plot(x_arrs[ind], y_arrs[ind], label=label_arrs[ind])

    if legend:
        axs.legend(title=legend_title)
      
    figure.suptitle(suptitle)  
    if tight_layout:
        figure.tight_layout()

    return figure, axs