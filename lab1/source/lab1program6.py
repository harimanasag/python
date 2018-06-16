import numpy as np

a = np.array([1,2,16,14,6,5,9,9,20,19,18])
counts = np.bincount(a)
print("Most frequent item is:")
print(np.argmax(counts))