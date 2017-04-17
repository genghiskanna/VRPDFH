from scipy.spatial.distance import euclidean
from statistics import mean
from copy import copy


def CalculateEuclidean(nodes):
    distance = []
    a_node = (0, 0)
    for loop, node in enumerate(nodes):
        b_node = (node.nodeX, node.nodeY)
        distance.append(euclidean(a_node, b_node))
        a_node = copy(b_node)

    return distance


def CalculateUtilization(nodes):
    initLoad = []
    for node in nodes:
        initLoad.append(node.initLoad)

    return mean(initLoad)
