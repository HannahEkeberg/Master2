from scipy.interpolate import splev, splrep
import numpy as np

class Tools:

    def interpolate(self, x, y, zeroPadding=False):
        if zeroPadding:
            x, y = self.zeroPadding(x,y)
        tck = splrep(x, y, s=0)
        x_new = np.linspace(1, 40, 1000)
        y_new = splev(x_new, tck, der=0)
        return x_new, y_new

    def zeroPadding(self, x, y):
        if x[0]!=0:
            zero_padding = np.linspace(0,x[0]-0.5,10)
            zeros_y = np.zeros((len(zero_padding)))
            x = np.concatenate((zero_padding, x))
            y = np.concatenate((zeros_y, y))
        return x, y
