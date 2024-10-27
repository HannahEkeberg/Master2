from scipy.interpolate import splev, splrep
import numpy as np

class Tools:

    def interpolate(self, x, y):
        tck = splrep(x, y, s=0)
        x_new = np.linspace(1, 40, 1000)
        y_new = splev(x_new, tck, der=0)
        return x_new, y_new
