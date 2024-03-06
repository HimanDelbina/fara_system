from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.views.decorators.csrf import requires_csrf_token, csrf_protect
from django.contrib import messages


def home(request):
    product_data = ProductModel.objects.all()
    company_data = CompanyModel.objects.all()
    service_data = ServiceModel.objects.all()
    camera_data = CameraModel.objects.all()
    camera_company_data = CameraCategoryModel.objects.all()
    program_data = ProgramModel.objects.all()
    activity_data = ActivityModel.objects.all()
    Card_home = CardHomeModel.objects.all()
    social_media = SocialMediaModel.objects.all()
    camera_filter = []
    Card_filter = []
    company_filter = []
    count_filter = 0
    company_filter = 0
    count = 0
    for data in camera_data:
        count += 1
        if count <= 10:
            camera_filter.append(data)
    for data in Card_home:
        count_filter += 1
        if count_filter <= 4:
            Card_filter.append(data)
    for data in company_data:
        company_filter += 1
        if company_filter <= 8:
            company_filter.append(data)
    context = {
        "product_data": product_data,
        "company_data": company_filter,
        "service_data": service_data,
        "camera_data": camera_data,
        "camera_filter": camera_filter,
        "program_data": program_data,
        "activity_data": activity_data,
        "camera_company_data": camera_company_data,
        "Card_home": Card_filter,
        "social_media": social_media,
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


def camera_select(request, pk):
    camera_data = CameraModel.objects.get(id=pk)
    context = {"camera_data": camera_data}
    return render(request, "core/camera_select.html", context)


@requires_csrf_token
def contact_me(request):
    if request.method == "POST":
        contact = ContactMeModel()
        username = request.POST.get("username")
        email = request.POST.get("email")
        phone_number = request.POST.get("phone_number")
        description = request.POST.get("description")
        contact.username = username
        contact.email = email
        contact.phone_number = phone_number
        contact.description = description
        contact.save()
        messages.info(request, "thanks for everything")
        return redirect("/")
    return render(request, "core/contact_me.html")
