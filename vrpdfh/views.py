from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from . import firstvrp
def index(request):
    return render(request, "index.html")


def process(request):
    myfile = request.FILES['excel_file']
    fs = FileSystemStorage()
    filename = fs.save(myfile.name, myfile)
    uploaded_file_url = fs.url(filename)
    print uploaded_file_url
    print filename
    chart_vrp_x,chart_vrp_y, util, total_distance = firstvrp.main("media/"+filename)
    return render(request, "process.html", {"chart_vrp_x": chart_vrp_x,"chart_vrp_y":chart_vrp_y,
                                            "util": util, "total_distance": total_distance})
