import pandas as pd
import numpy as np

from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline

import pickle
import json 

from newdata import newdata

newdata = newdata

with open('model.pkl', 'rb') as pickle_file:
    pipe = pickle.load(pickle_file)

predictions = pipe.predict_proba(newdata)
print(predictions)