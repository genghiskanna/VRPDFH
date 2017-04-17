import excelReadWrite
import vrp
from statistics import mean
from copy import copy


def main(filename):
    '''
    type_vrps
    linear
    linearskip
    dfh
    '''
    util = []
    total = []
    chart_vrp_x = []
    chart_vrp_y = []
    type_vrps = ["linear","linearskip","dfh"]
    for type_vrp in type_vrps:
        if type_vrp == "dfh":
            skip = True
            dfh = True
        if type_vrp == "linearskip":
            skip = True
            dfh = False
        if type_vrp == "linear":
            skip = False
            dfh = False

        nodes, depot = excelReadWrite.read_excel_file(filename)

        truck = 0
        final_nodes = []
        final_final_finalLoad = []

        distance = []
        average_distance = []
        total_distance = []

        utilization = []
        average_utilization = []

        chart_data_x = []
        chart_data_y = []

        while len(nodes) != 0:
            return_value = vrp.VRP(nodes, truck, depot, depot, skip, dfh)

            final_nodes.append(return_value["assigned_nodes_depot"])

            chart_nodes = return_value["assigned_nodes_depot"]

            distance.append(return_value["distance"])
            average_distance.append(mean(return_value["distance"]))
            total_distance.append(sum(return_value["distance"]))

            utilization.append(return_value["utilization"])

            final_final_finalLoad.append(return_value["final_finalLoad"])

            nodes = copy(return_value["nodes"])

            truck_temp_chart_x = [0]
            truck_temp_chart_y = [0]
            for loop,node in enumerate(chart_nodes):
                truck_temp_chart_x.append(node.nodeX)
                truck_temp_chart_y.append(node.nodeY)
            chart_data_x.append(truck_temp_chart_x)
            chart_data_y.append(truck_temp_chart_y)

            truck +=1
        chart_vrp_x.append(chart_data_x)
        chart_vrp_y.append(chart_data_y)
        average_utilization = mean(utilization)

        # flatenning nodes
        final_nodes = [y for x in final_nodes for y in x]
        distance = [y for x in distance for y in x]

        util.append(average_utilization)
        total.append(sum(total_distance))
        # writing to file type_vrp
        excelReadWrite.write_excel_file(type_vrp, final_nodes, distance, average_distance, total_distance,
                                        utilization, average_utilization)
    return chart_vrp_x,chart_vrp_y, util, total

if __name__ == "__main__":
    main()
