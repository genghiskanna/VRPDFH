import xlrd
import xlwt
from Nodes import Nodes
from copy import copy


def read_excel_file(filename):
    workbook = xlrd.open_workbook(filename)
    sheet = workbook.sheet_by_index(0)
    nodes = []
    temp_node = Nodes()
    depot = Nodes()
    for rows in range(sheet.nrows):
        print str(sheet.cell_value(rows, 0))
        if "pot" in str(sheet.cell_value(rows, 0)):
            depot.nodeNames = str(sheet.cell_value(rows, 0))
            depot.nodeId = int(sheet.cell_value(rows, 1))
            depot.nodeX = int(sheet.cell_value(rows, 2))
            depot.nodeY = int(sheet.cell_value(rows, 3))
            depot.nodePickup = int(sheet.cell_value(rows, 4))
            depot.nodeDelivery = int(sheet.cell_value(rows, 5))
        else:
            temp_node.nodeNames = str(sheet.cell_value(rows, 0))
            temp_node.nodeId = int(sheet.cell_value(rows, 1))
            temp_node.nodeX = int(sheet.cell_value(rows, 2))
            temp_node.nodeY = int(sheet.cell_value(rows, 3))
            temp_node.nodePickup = int(sheet.cell_value(rows, 4))
            temp_node.nodeDelivery = int(sheet.cell_value(rows, 5))
            nodes.append(copy(temp_node))

    return nodes, depot


def write_excel_file(type, nodes, distance, average_distance_per_truck, total_distance_per_truck, total_utilization_per_truck,
                     average_utilization_per_truck):

    # writing Question to excel sheet
    row = 0
    wb = xlwt.Workbook()
    ws = wb.add_sheet("answer", cell_overwrite_ok=True)
    ws.write(row, 0, type)
    row = 1
    # writing sheet description
    ws.write(row, 0, "Node Name")
    ws.write(row, 1, "Node Id")
    ws.write(row, 2, "Node X")
    ws.write(row, 3, "Node Y")
    ws.write(row, 4, "Node Pickup")
    ws.write(row, 5, "Node Delivery")
    ws.write(row, 6, "InitLoad")
    ws.write(row, 7, "FinalLoad")
    ws.write(row, 8, "Distance")
    ws.write(row, 9, "average_distance_per_truck")
    ws.write(row, 10, "total_distance_per_truck")
    ws.write(row, 11, "average_utilization_per_truck")
    ws.write(row, 12, "total_utilization_per_truck")

    row = 2
    for loop, node in enumerate(nodes):
        ws.write(row, 0, node.nodeNames)
        ws.write(row, 1, node.nodeId)
        ws.write(row, 2, node.nodeX)
        ws.write(row, 3, node.nodeY)
        ws.write(row, 4, node.nodePickup)
        ws.write(row, 5, node.nodeDelivery)
        ws.write(row, 6, node.initLoad)
        ws.write(row, 7, node.finalLoad)
        ws.write(row, 8, distance[loop])
        if "pot" in node.nodeNames:
            row += 3
        else:
            row += 1

    row = 2
    for loop, dist in enumerate(average_distance_per_truck):
        ws.write(row, 9, float(dist))
        ws.write(row, 10, float(total_distance_per_truck[loop]))
        ws.write(row, 12, float(total_utilization_per_truck[loop]))
        row += 1

    ws.write(2, 11, float(average_utilization_per_truck))
    ws.write(len(total_distance_per_truck) + 2, 10,
             sum(total_distance_per_truck))

    print "Saving The excel file"
    wb.save("media/"+type + "answer.xls")
    print "Successfully saved!"
