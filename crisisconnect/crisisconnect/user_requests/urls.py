from django.urls import path
from .views import create_request,retrieve_request,user_retrieve_request,specific_request_details,approved_retrieve_request,rejected_retrieve_request

urlpatterns = [path("create/", create_request,name="create_request"),
               path("list/",retrieve_request,name="list"),
               path("user-list/",user_retrieve_request,name="user-list"),
               path("approved/",approved_retrieve_request,name="approved_details"),
               path("rejected/",rejected_retrieve_request,name="rejected_details"),
               path("requestdetails/<int:pk>/",specific_request_details,name="requestdetails"),
               
               ]
