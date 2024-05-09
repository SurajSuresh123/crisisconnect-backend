from django.shortcuts import render
from .serializers import CreateRequestSerailizer, RetrieveRequestSerializer
from rest_framework.generics import CreateAPIView, ListAPIView,RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .models import UserRequest
from rest_framework import status
# Create your views here.


class CreateRequest(CreateAPIView):
    serializer_class = CreateRequestSerailizer
    # permission_classes = [
    #     IsAuthenticated,
    # ]

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data,status.HTTP_201_CREATED)


create_request = CreateRequest.as_view()


class RetrieveRequest(ListAPIView):
    serializer_class = RetrieveRequestSerializer

    queryset=UserRequest.objects.all()
    def list(self,request):
        user_request=self.get_queryset()
        if user_request.exists():
            serializer = self.get_serializer(user_request, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Requests Present"},status.HTTP_204_NO_CONTENT)

retrieve_request = RetrieveRequest.as_view()


class UserRetrieveRequest(ListAPIView):
    serializer_class = RetrieveRequestSerializer
    def get_queryset(self):
        return UserRequest.objects.filter(user=self.request.user)
    def user_list(self,request):
        user_request=self.get_queryset()
        if user_request.exists():
            serializer = self.get_serializer(user_request, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Requests Present"},status.HTTP_204_NO_CONTENT)


user_retrieve_request = UserRetrieveRequest.as_view()

class SpecificRequestDetails(RetrieveAPIView):
    serializer_class=RetrieveRequestSerializer
    queryset=UserRequest.objects.all()
    lookup_field='pk'

specific_request_details=SpecificRequestDetails.as_view()

class ApprovedRetrieveRequest(ListAPIView):
    serializer_class = RetrieveRequestSerializer

    def get_queryset(self):
        return UserRequest.objects.filter(approved=True)
    def list(self,request):
        user_request=self.get_queryset()
        if user_request.exists():
            serializer = self.get_serializer(user_request, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Approved Requests Present"},status.HTTP_204_NO_CONTENT)

approved_retrieve_request = ApprovedRetrieveRequest.as_view()

class RejectedRetrieveRequest(ListAPIView):
    serializer_class = RetrieveRequestSerializer

    def get_queryset(self):
        return UserRequest.objects.filter(approved=False)
    def list(self,request):
        user_request=self.get_queryset()
        if user_request.exists():
            serializer = self.get_serializer(user_request, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message":"No Requests Present"},status.HTTP_204_NO_CONTENT)

rejected_retrieve_request = RejectedRetrieveRequest.as_view()