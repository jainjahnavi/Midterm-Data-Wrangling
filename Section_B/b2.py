import numpy as np
import pandas as pd

a=np.array([[10,20,30],[40,50,60]])

#(i)
print("Mean of Each Column: ",np.mean(a,axis=1))

#(ii)
print("Output where a>25 ",a[a>25])