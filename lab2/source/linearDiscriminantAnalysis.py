from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
import matplotlib.pyplot as plt

digitsdataset = datasets.load_digits()

x=digitsdataset.data
y=digitsdataset.target

target_names = digitsdataset.target_names

#splitting the data into training and test data
x_train, x_test, y_train, y_test = train_test_split(x,y, test_size=0.4)

classifier = KNeighborsClassifier(n_neighbors=5)
classifier.fit(x_train, y_train)

test_prediction = classifier.predict(x_test)

lda = LinearDiscriminantAnalysis(n_components=2)
x_transform = lda.fit(x_test, test_prediction).transform(x)

plt.figure()

colors = ['navy', 'turquoise', 'darkorange']

for color, i, target_name in zip(colors, [0, 1, 2], target_names):
    plt.scatter(x_transform[y == i, 0], x_transform[y == i, 1], alpha=.8, color=color,
                label=target_name)
plt.legend(loc='best', shadow=False, scatterpoints=1)
plt.title('LDA of DIGITS dataset')

plt.show()