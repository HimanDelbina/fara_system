from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    product_data = ProductModel.objects.all()
    company_data = CompanyModel.objects.all()
    service_data = ServiceModel.objects.all()
    camera_data = CameraModel.objects.all()
    program_data = ProgramModel.objects.all()
    activity_data = ActivityModel.objects.all()
    camera_filter = []
    count = 0
    for data in camera_data:
        count += 1
        if count <= 10:
            camera_filter.append(data)

    context = {
        "product_data": product_data,
        "company_data": company_data,
        "service_data": service_data,
        "camera_data": camera_data,
        "camera_filter": camera_filter,
        "program_data": program_data,
        "activity_data": activity_data,
    }
    return render(request, "core/home.html", context)


def more_camera(request):
    camera_data = CameraModel.objects.all()
    context = {"camera_data": camera_data}
    return render(request, "core/morecamera.html", context)


def details_camera(request):
    camera_data = CameraModel.objects.all()
    context = {"camera_data": camera_data}
    return render(request, "core/details_camera.html", context)
