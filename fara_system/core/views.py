from django.shortcuts import render
from .models import *

# Create your views here.


def home(request):
    product_data = ProductModel.objects.all()
    company_data = CompanyModel.objects.all()
    service_data = ServiceModel.objects.all()
    camera_data = CameraModel.objects.all()
    camera_company_data = CameraCategoryModel.objects.all()
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
        "camera_company_data": camera_company_data,
    }
    return render(request, "core/home.html", context)


def more_camera(request):
    camera_data = CameraModel.objects.all()
    CATID = request.GET.get("category")
    camera_company_data = CameraCategoryModel.objects.all()
    if CATID:
        camera_data = CameraModel.objects.filter(category=CATID)
    else:
        camera_data = CameraModel.objects.filter(is_publish=True)
    context = {
        "camera_data": camera_data,
        "camera_company_data": camera_company_data,
    }
    return render(request, "core/morecamera.html", context)


def details_camera(request):
    camera_data = CameraModel.objects.all()
    context = {"camera_data": camera_data}
    return render(request, "core/details_camera.html", context)


def camera_select(request,pk):
    camera_data = CameraModel.objects.get(id=pk)
    context = {"camera_data": camera_data}
    return render(request, "core/camera_select.html", context)