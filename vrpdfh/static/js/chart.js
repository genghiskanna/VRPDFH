lineChartData_linear = {}; //declare an object
lineChartData_linear.datasets = []; // y

lineChartData_skip = {}; //declare an object
lineChartData_skip.datasets = []; // y

lineChartData_dfh = {}; //declare an object
lineChartData_dfh.datasets = []; // y

dataLine_linear = [];
dataLine_skip = [];
dataLine_dfh = [];



dataType = {};
before_data_type = [];
console.log(chart_vrp_x[0].length);
for(loop = 0; loop<chart_vrp_x[0].length;loop++){
    for(subloop = 0; subloop<chart_vrp_x[0][loop].length; subloop++){
        dataType.x = chart_vrp_x[0][loop][subloop];
        dataType.y = chart_vrp_y[0][loop][subloop];
        before_data_type.push(dataType);
        dataType = {};

    }
    dataLine_linear.push(before_data_type)
    before_data_type = [];
}


dataType = {};
before_data_type = [];
for(loop = 0; loop<chart_vrp_x[1].length;loop++){
    for(subloop = 0; subloop<chart_vrp_x[1][loop].length; subloop++){
        dataType.x = chart_vrp_x[1][loop][subloop];
        dataType.y = chart_vrp_y[1][loop][subloop];
        before_data_type.push(dataType);
        dataType = {};
    }
    dataLine_skip.push(before_data_type);
    before_data_type = [];
}


dataType = {};
before_data_type = [];
for(loop = 0; loop<chart_vrp_x[2].length;loop++){
    for(subloop = 0; subloop<chart_vrp_x[2][loop].length; subloop++) {
        dataType.x = chart_vrp_x[2][loop][subloop];
        dataType.y = chart_vrp_y[2][loop][subloop];
        before_data_type.push(dataType);
        dataType = {};
    }
    dataLine_dfh.push(before_data_type);
    before_data_type = [];
}

label = [
    "Truck 1",
    "Truck 2",
    "Truck 3",
    "Truck 4",
    "Truck 5",
    "Truck 6",
    "Truck 7",
    "Truck 8",
    "Truck 9",
    "Truck 10",
    "Truck 11",
    "Truck 12",
    "Truck 13",
    "Truck 14",
    "Truck 15",
    "Truck 16",
];



color = [
    "rgba(255,0,255,1)",
    "rgba(255,0,0,1)",
    "rgba(0,255,0,1)",
    "rgba(0,0,255,1)",
    "rgba(255,0,255,1)",
    "rgba(0,128,128,1)",
    "rgba(0,0,128,1)",
    "rgba(220,20,60,1)",
    "rgba(0,255,255,1)",
    "rgba(127,255,212,1)",
    "rgba(106,90,205,1)",
    "rgba(128,0,128,1)",
    "rgba(219,112,147,1)",
    "rgba(139,69,19,1)",
    "rgba(112,128,144,1)",
    "rgba(105,105,105,1)",
    "rgba(107,142,35,1)",
    "rgba(124,252,0,1)"
]


for (line=0;line<chart_vrp_x[0].length;line++){
    lineChartData_linear.datasets.push({})
    lineChartData_linear.datasets[line].data = dataLine_linear[line];
    lineChartData_linear.datasets[line].label = label[line];
    lineChartData_linear.datasets[line].fill = false;
    lineChartData_linear.datasets[line].lineTension = 0;
    lineChartData_linear.datasets[line].borderColor = color[line];
}

for (line=0;line<chart_vrp_x[1].length;line++){
    lineChartData_skip.datasets.push({})
    lineChartData_skip.datasets[line].data = dataLine_skip[line];
    lineChartData_skip.datasets[line].label = label[line];
    lineChartData_skip.datasets[line].fill = false;
    lineChartData_skip.datasets[line].lineTension = 0;
    lineChartData_skip.datasets[line].borderColor = color[line];
}


for (line=0;line<chart_vrp_x[2].length;line++){
    lineChartData_dfh.datasets.push({})
    lineChartData_dfh.datasets[line].data = dataLine_dfh[line];
    lineChartData_dfh.datasets[line].label = label[line];
    lineChartData_dfh.datasets[line].fill = false;
    lineChartData_dfh.datasets[line].lineTension = 0;
    lineChartData_dfh.datasets[line].borderColor = color[line];
}
ctx = document.getElementById("line-chart-linear").getContext("2d");
myLineChart = new Chart(ctx, {
     type: 'line',
     data: lineChartData_linear,
    options: {
        scales: {
            xAxes: [{
                type: 'linear',
                position: 'bottom'
            }]
        }
    }
});


ctx1 = document.getElementById("line-chart-skip").getContext("2d");
myLineChart = new Chart(ctx1, {
     type: 'line',
     data: lineChartData_skip,
    options: {
        scales: {
            xAxes: [{
                type: 'linear',
                position: 'bottom'
            }]
        }
    }
});


ctx2 = document.getElementById("line-chart-dfh").getContext("2d");
myLineChart = new Chart(ctx2, {
     type: 'line',
     data: lineChartData_dfh,
    options: {
        scales: {
            xAxes: [{
                type: 'linear',
                position: 'bottom'
            }]
        }
    }
});


barctx = document.getElementById("bar-chart").getContext("2d");
myBarChart = new Chart(barctx, {
     type: 'bar',
     data: {
         labels: ["Simple LSA","LSA with skip", "DFH"],
         datasets:[{
             data:util,
             label:"Average Utilization",
             backgroundColor:"rgba(255,0,255,1)"
         }]
     }
});


barctx = document.getElementById("bar-chart-distance").getContext("2d");
myBarChart = new Chart(barctx, {
     type: 'bar',
     data: {
         labels: ["Simple LSA","LSA with skip", "DFH"],
         datasets:[{
             data:total_distance,
             label:"Total Distance Travelled",
             backgroundColor:"rgba(0,0,255,1)"
         }]
     }
});