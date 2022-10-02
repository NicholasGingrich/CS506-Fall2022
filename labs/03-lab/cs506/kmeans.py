from collections import defaultdict
from math import inf
import random
import csv


def get_centroid(points):
    """
    Accepts a list of points, each with the same number of dimensions.
    (points can have more dimensions than 2)
    
    Returns a new point which is the center of all the points.
    """
    ave_dims = [0 for i in range(len(points[0]))]
    for i in range(len(points)):
        for j in range(len(points[i])):
            ave_dims[j] += points[i][j]

    for i in range(len(ave_dims)):
        ave_dims[i] = ave_dims[i]/len(points)

    return ave_dims

print(get_centroid([[1,1,1],[2,2,2],[6,6,6]]))



def get_centroids(dataset, assignments):
    """
    Accepts a dataset and a list of assignments; the indexes 
    of both lists correspond to each other.
    Compute the centroid for each of the assigned groups.
    Return `k` centroids in a list
    """
    centr_dict = {}
    cent_list = []
    for i in len(assignments):
        if centr_dict[assignments[i]] == None:
            centr_dict[assignments[i]] = [dataset[i]]
        else:
            centr_dict[assignments[i]] = centr_dict[assignments[i]] + [dataset[i]]

        for key, val in centr_dict:
            cent_list.append(get_centroid(val))
            


def assign_points(data_points, centers):
    """
    """
    assignments = []
    for point in data_points:
        shortest = inf  # positive infinity
        shortest_index = 0
        for i in range(len(centers)):
            val = distance(point, centers[i])
            if val < shortest:
                shortest = val
                shortest_index = i
        assignments.append(shortest_index)
    return assignments


def distance(a, b):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)


def distance_squared(a, b):
    return distance(a,b) ** 2


def cost_function(clustering):
    all_cost = 0
    for cluster in clustering:
        mean = sum(cluster)/len(cluster)
        cost = 0
        for point in cluster:
            cost += distance_squared(point, mean)
        all_cost += cost
    
    return all_cost


def generate_k(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    """
    points = []
    rand_range = len(dataset)
    for i in range(k):
        points.append(dataset[random.randint(0,rand_range)])

    return points


def generate_k_pp(dataset, k):
    """
    Given `data_set`, which is an array of arrays,
    return a random set of k points from the data_set
    where points are picked with a probability proportional
    to their distance as per kmeans pp
    """
    points = []
    count = 0
    for i in range(k):
        for point in dataset:
            prob = cost_function(point)
            if random.random() <= prob:
                points.append(point)
                count += 1
        if count > k:
            return points
    
    return points

def _do_lloyds_algo(dataset, k_points):
    assignments = assign_points(dataset, k_points)
    old_assignments = None
    while assignments != old_assignments:
        new_centers = get_centroids(dataset, assignments)
        old_assignments = assignments
        assignments = assign_points(dataset, new_centers)
    clustering = defaultdict(list)
    for assignment, point in zip(assignments, dataset):
        clustering[assignment].append(point)
    return clustering


def k_means(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")
    
    k_points = generate_k(dataset, k)
    return _do_lloyds_algo(dataset, k_points)


def k_means_pp(dataset, k):
    if k not in range(1, len(dataset)+1):
        raise ValueError("lengths must be in [1, len(dataset)]")

    k_points = generate_k_pp(dataset, k)
    return _do_lloyds_algo(dataset, k_points)
