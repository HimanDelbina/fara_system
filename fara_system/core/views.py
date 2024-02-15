from django.shortcuts import render

# Create your views here.
def home(request):
    context = {"test":"Hello World"}
    # return render(request, "core/index.html", context)
    return render(request, "core/home.html", context)