import matplotlib.pyplot as plt
import os


def save_fig(fig, destination, name):
    output_path = os.path.join(destination, name)
    fig.savefig(output_path + "_transparent", transparent=True)
    fig.savefig(output_path, transparent=False)