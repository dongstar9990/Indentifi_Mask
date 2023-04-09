# pip install numpy
import numpy as np
# pip install pandas

import pandas as pd

#pip install matplotlib
import matplotlib.pyplot as plt
import os

# path of image and annotations

input_data_path='/content/gdriver/MyDrive/ML/Data/images'
annotations_path="/content/gdriver/MyDrive/ML/Data/annotations"
images=[*os.listdir("/content/gdriver/MyDrive/ML/Data/images")]
#*os.listdir : tra ve mot danh sach chuaa ten cua cac mua duoc cung cap boi duong dan
output_data_path="."
