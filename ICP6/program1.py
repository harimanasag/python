from sklearn import datasets
from sklearn import svm
from sklearn.naive_bayes import GaussianNB
# Implementing Naïve Bayes method using scikit-learn library
from sklearn.model_selection import train_test_split

#Using iris dataset available in the package
irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target

#split the data for training and testing cross validation
# train data =
# test data = score/quality
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

model=GaussianNB()
model.fit(x_train,y_train)
#quality of cluster
print(model.score(x_test,y_test))