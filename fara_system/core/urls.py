from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("/more_camera", more_camera, name="more_camera"),
    path("/detailscamera", details_camera, name="detailscamera"),
    path("camera_select/<int:pk>", camera_select),
    path("/contact_me", contact_me, name="contact_me"),
    # path("project/<int:pk>", project_select),
]
