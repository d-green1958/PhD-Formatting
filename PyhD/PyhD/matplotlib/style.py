import matplotlib.pyplot as plt
from cycler import cycler


def apply_style():
    """Apply consistent styling to matplotlib figures."""
    plt.rcParams.update(
        {
            "font.family": "serif",
            "figure.figsize": (6, 4),  # Default figure size
            "font.size": 12,  # Base font size
            "axes.titlesize": 14,  # Title font size
            "axes.labelsize": 12,  # Axes label font size
            "legend.fontsize": 10,  # Legend font size
            "xtick.labelsize": 10,  # X-axis tick font size
            "ytick.labelsize": 10,  # Y-axis tick font size
            "lines.linewidth": 2,  # Line width
            "axes.grid": True,  # Enable grid
            "grid.alpha": 0.5,  # Grid transparency
            "grid.linestyle": "--",  # Grid line style
            "savefig.dpi": 600,  # High-quality figures
            "mathtext.fontset": "cm",
        }
    )

    default_cycler = (
        cycler(color=["black", "red", "blue", "green", "orange", "purple"])
        + cycler(linestyle=["-", "-", "-", "-", "-", "-"])
        + cycler(alpha=[0.7, 0.7, 0.7, 0.7, 0.7, 0.7])
    )
    plt.rc("axes", prop_cycle=default_cycler)

    plt.rcParams["image.cmap"] = (
        "viridis"  # Change 'viridis' to your preferred colormap
    )
