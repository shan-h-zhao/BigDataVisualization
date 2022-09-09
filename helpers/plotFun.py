'''
Purpose: This program provides demo visualizations one can create using wejo data
Author: szhao
Date: 9/7/2022
'''
'''
plotFun.py provides some sample plot functions
'''
import matplotlib.pyplot as plt
from matplotlib.collections import PathCollection
from matplotlib.legend_handler import HandlerPathCollection, HandlerLine2D


# plot records using lat/lng
def plotPoints(df):
    # ax = plt.scatter(df["location.longitude"].values, df["location.latitude"].values, color = "blue", s = 0.5, alpha=0.1)
    ax = plt.scatter(df["location_longitude"], df["location_latitude"], color = "blue", s = 0.5, alpha=0.1)
    ax.axes.set_title("Coordinates of Data")
    ax.figure.set_size_inches(6, 5)

def plotPoints2(df):
    # ax = plt.scatter(df["location.longitude"].values, df["location.latitude"].values, color = "blue", s = 0.5, alpha=0.1)
    ax = plt.scatter(df["location.longitude"], df["location.latitude"], color = "blue", s = 0.5, alpha=0.1)
    ax.axes.set_title("Coordinates of Data")
    ax.figure.set_size_inches(6, 5)

def plotPointsByCategory(df, category):
    groups = df.groupby(category)
    fig, ax = plt.subplots(figsize = (20, 12))
    ax.margins(0.05)
    for name, group in groups:
        ax.plot(group.location_longitude, group.location_latitude, marker='o', linestyle='', ms=12, label=name, alpha=0.1)
        ax.legend()
    def update(handle, orig):
        handle.update_from(orig)
        handle.set_alpha(1)
    plt.legend(handler_map={PathCollection : HandlerPathCollection(update_func= update), plt.Line2D : HandlerLine2D(update_func = update)})
    plt.show()


# ref: https://medium.com/the-data-science-publication/how-to-plot-geospatial-data-with-python-d788ee54dcd1


