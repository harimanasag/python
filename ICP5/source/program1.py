import numpy as np
import matplotlib.pyplot as plt

xValues = np.array([0,1,2,3,4,5,6,7,8,9])
yValues = np.array([1,3,2,5,7,8,8,9,10,12])

#mean value of x and y
meanOfX = xValues.mean()
meanOfy = yValues.mean()

#calculating slope
slope = np.sum((xValues - meanOfX)*(yValues - meanOfy))/np.sum(np.square(xValues-meanOfX))

#calculating intercept
intercept = meanOfy - (slope * meanOfX)

#y output
yOutput = (slope * xValues) + intercept


plt.plot(xValues,yValues)  # plotting the line made by linear regression
#plt.show()

plt.plot(xValues, yOutput)
plt.show()



