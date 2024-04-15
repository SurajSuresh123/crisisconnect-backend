from django.urls import path
from .views import create_feedback,retrieve_feedback,specific_feedback_details,user_retrieve_feedback

urlpatterns = [path("create/", create_feedback,name="create_feedback"),
              path("feedback-list/",retrieve_feedback,name="feedback-list"),
              path("user-feedback/",user_retrieve_feedback,name="user-grievance"),
              path("feedbackdetails/<int:pk>/",specific_feedback_details,name="feedbackdetails")
              ]