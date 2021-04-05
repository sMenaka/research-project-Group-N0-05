from numpy import loadtxt
import numpy as np
from keras.models import Sequential,load_model
from keras.layers import Dense
from sklearn import model_selection
import MFCC as mfcc

mdl = load_model(r'trained-2.h5')

def predict(path):
    global mdl
    features=mfcc.getMFCC(path)
    predictions = mdl.predict_classes(features)
    present = mdl.predict_proba(features)
    return predictions