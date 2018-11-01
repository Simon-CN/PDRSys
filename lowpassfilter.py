from scipy import signal
import numpy as np
import math


def lowPassFilter(x,sf=100,lsf=15):
    b,a = signal.butter(3, 2 * lsf / sf, "low")
    res = signal.filtfilt(b, a, np.ravel(x))
    return res
