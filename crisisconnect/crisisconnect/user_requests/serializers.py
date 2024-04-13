from rest_framework import serializers
from .models import UserRequest


class CreateRequestSerailizer(serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = ["id","type", "request_desc", "document", "medical_document"]


class RetrieveRequestSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")

    def get_username(self,obj:UserRequest):
        return obj.user.username
    
    class Meta:
        model = UserRequest
        fields = ["id","username","type", "request_desc", "document", "medical_document","created_at"]


    