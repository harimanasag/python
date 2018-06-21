import numpy as np
import matplotlib.pyplot as plt
import random

def create_cluster(X, centroid_pts):
    cluster = {}
  # read about lambdas and np.linalg.form
  # https://stackoverflow.com/questions/32141856/is-norm-equivalent-to-euclidean-distance ,
  # here we are using order 1 to calculate normalized distance
    for x in X:
        value = min([(i[0],np.linalg.norm(x - centroid_pts[i[0]]))for i in enumerate(centroid_pts)], key=lambda s:s[1])[0]
        try:
            cluster[value].append(x)
        except:
            cluster[value] = [x]
    return cluster


def calculate_new_center(cluster):
    keys =sorted(cluster.keys())
    newmu = np.array([(np.mean(cluster[k],axis = 0))for k in keys])
    return newmu

def matched(new_centroids, old_centroids):
    return (set([tuple(a)for a in new_centroids]) == set([tuple(a)for a in old_centroids]))

def Apply_Kmeans(X, K, N):
    # selecting random centroids from dataset and by number of clusters.
    old_centroids = np.random.randint(N, size = K)
    old_centroid_pts = np.array([X[i]for i in old_centroids])

    print("old :",old_centroids)
    print(old_centroid_pts)

    cluster_info = create_cluster(X, old_centroid_pts)

    print("Initial cluster information:")
    print(cluster_info)

    new_centroid_pts=calculate_new_center(cluster_info)
    print("new :", new_centroid_pts)
    itr = 0
    print("Graph after selecting initial clusters with initial centroids:")
    plot_cluster(old_centroid_pts,cluster_info,itr)
    while not matched(new_centroid_pts, old_centroid_pts):
        itr = itr + 1
        old_centroid_pts = new_centroid_pts
        cluster_info = create_cluster(X,new_centroid_pts)
        plot_cluster(new_centroid_pts, cluster_info,itr)
        new_centroid_pts = calculate_new_center(cluster_info)

    print("Results after final iteration:")
    plot_cluster(new_centroid_pts, cluster_info, itr)
    return

def plot_cluster(mu,cluster, itr):
	#color allocated for clusters
    color = 10 * ['r.','g.','k.','c.','b.','m.']
    print('Iteration number : ',itr)
    for l in cluster.keys():
        for m in range(len(cluster[l])):
            plt.plot(cluster[l][m][0], cluster[l][m][1], color[l], markersize=10)
    plt.scatter(mu[:,0],mu[:,1],marker = 'x', s = 150, linewidths = 5, zorder = 10)
    plt.show()

def init_graph(N, p1, p2):
	#array to choose random values
    X = np.array([(random.choice(p1),random.choice(p2))for i in range(N)])
    return X


def Simulate_Clusters():
    print(".........Starting Cluster Simulation.........")
    K = int(input('Enter the number of Clusters.......'))
    print('Now Enter the bounds for choosing uniform value....\n')
	#width of the T-shirt sizes
    p1 = np.array([32,33,36,40,39,31,35.5,30.3,34.3,32.7,39.8,37.2,31.4,38.8,32.6,34.7,35.1,37.5,36.2,39.8])
	#height of the person
    p2 = np.array([5.4,5.6,5.8,5.10,6,6.2])
    X = init_graph(len(p1), p2, p1)
    plt.scatter(X[:, 0], X[:, 1])
    plt.show()
	#calling K-means algorithm
    Apply_Kmeans(X, K, len(X))


if __name__ == '__main__':
    Simulate_Clusters()