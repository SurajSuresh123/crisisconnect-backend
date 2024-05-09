from django.shortcuts import render
from .serializers import CreateFeedbackSerializer,RetrieveFeedbackSerializer
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .models import feedback
from rest_framework import status
from .permission import IsCollector
# Create your views here.
class CreateFeedback(CreateAPIView):
    serializer_class = CreateFeedbackSerializer
    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data,status.HTTP_201_CREATED)

create_feedback=CreateFeedback.as_view()

class RetrieveFeedback(ListAPIView):
    serializer_class=RetrieveFeedbackSerializer
    permission_classes =[IsAuthenticated,IsCollector,]
    queryset=feedback.objects.all()

    def list(self,request):
        feedback=self.get_queryset()
        if feedback.exists():
            serializer = self.get_serializer(feedback, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Feedbacks"},status.HTTP_204_NO_CONTENT)

retrieve_feedback = RetrieveFeedback.as_view()

class UserRetrieveFeedback(ListAPIView):
    serializer_class = RetrieveFeedbackSerializer
    permission_classes = [
        IsAuthenticated
    ]
    def get_queryset(self):
        return feedback.objects.filter(user=self.request.user)
    def user_list(self,request):
        feedback=self.get_queryset()
        if feedback.exists():
            serializer = self.get_serializer(feedback, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Feedbacks made"},status.HTTP_204_NO_CONTENT)


user_retrieve_feedback = UserRetrieveFeedback.as_view()

class SpecificFeedbackDetails(RetrieveAPIView):
    serializer_class=RetrieveFeedbackSerializer
    permission_classes=[IsAuthenticated,]
    queryset=feedback.objects.all()
    lookup_field='pk'

specific_feedback_details=SpecificFeedbackDetails.as_view()

