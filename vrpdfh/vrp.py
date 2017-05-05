from operator import attrgetter
from statistics import mean
from copy import copy
import SupportUtility
from excelReadWrite import write_excel_file


def VRP(nodes, truck, depot, first_depot, skip, dfh):
    if dfh:
        nodes = sorted(nodes, key=attrgetter("nodeDelivery"), reverse=True)
    else:
        nodes = sorted(nodes, key=attrgetter("nodeY"), reverse=True)

    print "\n\n\n---------------------Truck %d-------------------\n\n\n" % (truck)

    initLoad, finalLoad, assigned_nodes = AssignNodesRecursively(
        nodes, skip)
    # do it again after sorting nodeX
    assigned_nodes = sorted(assigned_nodes,
                            key=attrgetter("nodeX"), reverse=False)
    print "after X sort"
    initLoad, finalLoad, assigned_nodes = AssignNodesRecursively(
        assigned_nodes, skip)

    print "\n************************End of recursion****************************\n"
    final_finalLoad = 0

    print "len(assigned_nodes) %d" % (len(assigned_nodes))
    for i in assigned_nodes:
        nodes.remove(i)
        print "Removed %s from nodes" % (i.nodeNames)
    assigned_nodes_depot = copy(assigned_nodes)
    assigned_nodes_depot.append(copy(depot))
    # assigned_nodes_depot.insert(0, first_depot)
    for node in assigned_nodes_depot:
        if "pot" in node.nodeNames:
            node.initLoad = initLoad
            initLoad = finalLoad
        else:
            final_finalLoad += node.nodePickup
            node.initLoad = initLoad
            finalLoad = initLoad - node.nodeDelivery + node.nodePickup
            node.finalLoad = finalLoad
            initLoad = finalLoad
    distance = SupportUtility.CalculateEuclidean(assigned_nodes_depot)
    utilization = SupportUtility.CalculateUtilization(assigned_nodes_depot)
    return {"assigned_nodes_depot": assigned_nodes_depot, "assigned_nodes": assigned_nodes,
            "nodes": nodes, "final_finalLoad": final_finalLoad, "distance": distance,
            "utilization": utilization}


def AssignNodesRecursively(nodes, skip):
    recursive_nodes = []
    prev_recursive_nodes = []
    initLoad, assigned_nodes = CalculateInitLoad(nodes, skip)
    runIterative = 5
    for node in assigned_nodes:
        print "before recursion Node %d" % (node.nodeId)
    while runIterative:
        temp_initLoad = initLoad
        for node in assigned_nodes:
            finalLoad = temp_initLoad - node.nodeDelivery + node.nodePickup
            temp_initLoad = finalLoad
            if finalLoad > 100:
                initLoad -= assigned_nodes.pop().nodeDelivery
                break
        runIterative -= 1

    for node in assigned_nodes:
        print "after recursion Node %d" % (node.nodeId)
    return initLoad, finalLoad, assigned_nodes


def CalculateInitLoad(nodes, skip):
    skipFlag = 0
    initLoad = 0
    assigned_nodes = []
    if skip:
        for node in nodes:
            if (initLoad + node.nodeDelivery) <= 100:
                initLoad += node.nodeDelivery
                assigned_nodes.append(node)
                '''
            elif skipFlag < 3:
                skipFlag += 1
            else:
                break
                '''
    else:
        for node in nodes:
            if (initLoad + node.nodeDelivery) <= 100:
                initLoad += node.nodeDelivery
                assigned_nodes.append(node)
            else:
                break

    return initLoad, assigned_nodes
