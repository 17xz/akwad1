

from django.urls import path, include
from . import views

app_name = "test1"
urlpatterns = [


path("",views.Index.as_view()),
path("details/<int:pk>/",views.detailsDetailView.as_view(), name='details'),
path("help",views.Index2.as_view()),

]