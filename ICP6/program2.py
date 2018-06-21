import pandas
import pylab as pl
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA
# reading the CSV file
variables = pandas.read_csv('sample_stocks.csv')
#loading the CSV file field values to X and Y variables
X = variables[['dividendyield']]
Y = variables[['returns']]

Nc = range(1, 20)
kmeans = [KMeans(n_clusters=i) for i in Nc]

score = [kmeans[i].fit(Y).score(Y) for i in range(len(kmeans))]

pl.plot(Nc,score)
pl.xlabel('Number of Clusters')
pl.ylabel('Score')
pl.title('Elbow Curve')
pl.show()

pca = PCA(n_components=1).fit(Y)
#To project each row of your data into the vector space
pca_c = pca.transform(X)
pca_d = pca.transform(Y)

#applying kmeans algorithm for cluster size 3
kmeans=KMeans(n_clusters=3)
kmeansoutput=kmeans.fit(Y)

#Displying 3 Cluster K-Means
pl.figure('3 Cluster K-Means')
pl.scatter(pca_c[:, 0], pca_d[:, 0], c=kmeansoutput.labels_)
pl.xlabel('Dividend Yield')
pl.ylabel('Returns')
pl.title('3 Cluster K-Means')
pl.show()