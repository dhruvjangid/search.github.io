from django.urls import path
from .import views
urlpatterns = [
    path("",views.index,name = "index"),
    path("dhruv" ,views.dhruv , name = "dhruv"),
    path("<str:name>",views.greet ,name ="greet" )

]
