from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("/more_camera", more_camera, name="more_camera"),
    path("/detailscamera", details_camera, name="detailscamera"),
    # path("project/<int:pk>", project_select),
]
