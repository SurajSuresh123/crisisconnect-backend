from django.shortcuts import render
from .serializers import CreateSurveySerializer,RetrieveSurveySerializer
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Survey
from rest_framework import status
# Create your views here.

class CreateSurvey(CreateAPIView):
    serializer_class = CreateSurveySerializer
    permission_classes = [
        IsAuthenticated,
    ]
    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        created_by=str(request.user.username)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user,created_by=created_by)
        return Response(serializer.data,status.HTTP_201_CREATED)

create_survey=CreateSurvey.as_view()

class RetrieveUserSurvey(ListAPIView):
    serializer_class=CreateSurveySerializer
    permission_classes =[IsAuthenticated,]
    
    def get_queryset(self):
        return Survey.objects.filter(user=self.request.user)

    def list(self,request):
        survey=self.get_queryset()
        if survey.exists():
            serializer = self.get_serializer(survey, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Survey details"},status.HTTP_204_NO_CONTENT)
retrieve_user_survey = RetrieveUserSurvey.as_view()   

class SpecificSurveyDetails(RetrieveAPIView):
    serializer_class=RetrieveSurveySerializer
    permission_classes=[IsAuthenticated,]
    queryset=Survey.objects.all()
    lookup_field='pk'

specific_survey_details=SpecificSurveyDetails.as_view()