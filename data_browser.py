import numpy as np
import pandas as pd
import tensorflow as tf
import sys
import os

train_data = "data/train_dataset.csv"
tets_data = "data/test_dataset.csv"

df_train = pd.read_csv(train_data)
df_test = pd.read_csv(tets_data)

print(df_train)
print(pd.unique(df_train["director_name"]))
