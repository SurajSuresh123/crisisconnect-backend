from django.urls import path
from .views import create_request,retrieve_request,user_retrieve_request,specific_request_details

urlpatterns = [path("create/", create_request,name="create_request"),
               path("list/",retrieve_request,name="list"),
               path("user-list/",user_retrieve_request,name="user-list"),
               path("requestdetails/<int:pk>/",specific_request_details,name="requestdetails")]
