from django.shortcuts import render
from .serializers import CreateGrievanceSerializer, RetrieveGrievanceSerializer
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from .models import Grievance
from rest_framework import status
from .permission import IsWardMember
from rest_framework.views import APIView
# Create your views here.
class CreateGrievance(CreateAPIView):
    serializer_class = CreateGrievanceSerializer
    permission_classes = [
        IsAuthenticated,
    ]

    def create(self, request: Request) -> Response:
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save(user=self.request.user)
        return Response(serializer.data, status.HTTP_201_CREATED)


create_grievance = CreateGrievance.as_view()


class RetrieveGrievance(ListAPIView):
    serializer_class = RetrieveGrievanceSerializer
    queryset = Grievance.objects.all()

    def list(self, request):
        grievance = self.get_queryset()
        if grievance.exists():
            serializer = self.get_serializer(grievance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"Message": "No Grievances"}, status.HTTP_204_NO_CONTENT)


retrieve_grievance = RetrieveGrievance.as_view()


class UserRetrieveGrievance(ListAPIView):
    serializer_class = RetrieveGrievanceSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Grievance.objects.filter(user=self.request.user)

    def user_list(self, request):
        grievance = self.get_queryset()
        if grievance.exists():
            serializer = self.get_serializer(grievance, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(
                {"Message": "No Grievances made"}, status.HTTP_204_NO_CONTENT
            )


user_retrieve_grievance = UserRetrieveGrievance.as_view()


class SpecificGrievanceDetails(APIView):
    
    def get(self, request, pk):
        try:
            grievance = Grievance.objects.filter(request_id=pk)
            serializer = RetrieveGrievanceSerializer(grievance,many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Grievance.DoesNotExist:
            return Response({"Message": "Grievance not found"}, status=status.HTTP_404_NOT_FOUND)

specific_grievance_details = SpecificGrievanceDetails.as_view()