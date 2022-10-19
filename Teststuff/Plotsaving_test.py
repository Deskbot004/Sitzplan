import matplotlib.pyplot as plt
import numpy as np
import pickle


def create_image():
    ax = plt.subplot(111)
    x = np.linspace(0, 10)
    y = np.exp(x)
    plt.plot(x, y)
    with open('myplot.pkl','wb') as fid:
        pickle.dump(ax, fid)


def show_image():
    with open('myplot.pkl','rb') as fid:
        ax = pickle.load(fid)
    plt.show()


create_image()
show_image()