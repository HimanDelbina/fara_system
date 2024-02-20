from django.urls import path
from .views import *

urlpatterns = [
    path("", home, name="home"),
    path("/more_camera", more_camera, name="more_camera"),
    path("/details_camera", details_camera, name="details_camera"),
    # path("project/<int:pk>", project_select),
]