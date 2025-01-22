import matplotlib.pyplot as plt
from ..style import apply_style
import numpy as np


def landscape_fig(
    fig_name=None,
    x_label=None,
    y_label=None,
    title=None,
    x_arrs=None,
    y_arrs=None,
    linestyle_arrs=None,
    markerstyle_arrs=None,
    label_arrs=None,
    legend_handles=None,
    legend=False,
    legend_title=None,
    tight_layout=False,
    suptitle=None,
    dpi=None,
    linewidth=None,
    color_arrs=None,
):
    apply_style()
  
    figure = plt.figure(figsize=(6, 4), num=fig_name, dpi=dpi)
    axs = figure.gca()

    axs.set_title(title)
    axs.set_xlabel(x_label)
    axs.set_ylabel(y_label)
    
    colors_defined=False

    if x_arrs is not None:
        if label_arrs is None:
            label_arrs = np.full(len(x_arrs), "")
        if linestyle_arrs is None:
            linestyle_arrs = np.full(len(x_arrs), "-")
        if markerstyle_arrs is None:
            markerstyle_arrs = np.full(len(x_arrs), "")
        
        if color_arrs is not None:
            colors_defined = True
        
            
        for ind, _ in enumerate(x_arrs):
            if colors_defined:
                axs.plot(
                    x_arrs[ind],
                    y_arrs[ind],
                    label=label_arrs[ind],
                    linestyle=linestyle_arrs[ind],
                    marker=markerstyle_arrs[ind],
                    linewidth=linewidth,
                    color=color_arrs[ind],
                )
            else:
                axs.plot(
                    x_arrs[ind],
                    y_arrs[ind],
                    label=label_arrs[ind],
                    linestyle=linestyle_arrs[ind],
                    marker=markerstyle_arrs[ind],
                    linewidth=linewidth,
                )

    if legend:
        if legend_handles == None:
            axs.legend(title=legend_title)
        else:
            axs.legend(handles=legend_handles, title=legend_title)


    figure.suptitle(suptitle)
    if tight_layout:
        figure.tight_layout()

    return figure, axs
