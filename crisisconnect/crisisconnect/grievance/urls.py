from django.urls import path
from .views import create_grievance,retrieve_grievance,user_retrieve_grievance,specific_grievance_details

urlpatterns = [path("create/", create_grievance,name="create_grievance"),
              path("grievance-list/",retrieve_grievance,name="grievance-list"),
              path("user-grievance/",user_retrieve_grievance,name="user-grievance"),
              path("grievancedetails/<int:pk>/",specific_grievance_details,name="grievancedetails")
              ]