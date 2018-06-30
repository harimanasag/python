from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

#Loading iris dataset
irisdataset=datasets.load_iris()

#getting the data and response of the dataset
x=irisdataset.data
y=irisdataset.target

#split the data for training and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

#Applying K Neighbors Classifier
model= KNeighborsClassifier(n_neighbors=5)
model.fit(x_train,y_train)

y_predictor=model.predict(x_test)

print("Accuracy Score: ",metrics.accuracy_score(y_test,y_predictor))

k_range = range(1,50)
scores = [ ]

for k in k_range:
    knc = KNeighborsClassifier(n_neighbors=k)
    knc.fit(x_train,y_train)
    y_pred = knc.predict(x_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))

plt.plot(k_range,scores)
plt.xlabel("value of k")
plt.ylabel("testing accuracy")
plt.show()