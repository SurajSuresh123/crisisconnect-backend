from django.urls import path
from .views import create_survey,retrieve_user_survey,specific_survey_details

urlpatterns = [path("create/", create_survey,name="create_survey"),
              path("user-survey/",retrieve_user_survey,name="user-survey"),
              path("surveydetails/<int:pk>/",specific_survey_details,name="surveydetails")
              ]
