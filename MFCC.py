import os
import csv
import speechpy
import numpy as np
import scipy.io.wavfile as wav

import test

def getMFCC(path):
    sample_rate, samples = wav.read("source/decoded.wav")
    data=speechpy.feature.mfcc(samples, 1024, frame_length=0.100, frame_stride=0.01, num_cepstral=13, num_filters=40, fft_length=512, low_frequency=0, high_frequency=None, dc_elimination=True)
    return data