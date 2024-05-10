from rest_framework import serializers
from .models import UserRequest


class CreateRequestSerailizer(serializers.ModelSerializer):

    class Meta:
        model = UserRequest
        fields = ["id","type", "request_desc", "document", "medical_document"]


class RetrieveRequestSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")
    address=serializers.SerializerMethodField("get_address")
    email=serializers.SerializerMethodField("get_email")
    phone_no=serializers.SerializerMethodField("get_phone_no")
    def get_username(self,obj:UserRequest):
        return obj.user.username
    def get_address(self,obj:UserRequest):
        return obj.user.address
    def get_email(self,obj:UserRequest):
        return obj.user.email
    def get_phone_no(self,obj:UserRequest):
        return obj.user.phone_number
    class Meta:
        model = UserRequest
        fields = ["id","username","address","email","phone_no","type", "request_desc", "document", "medical_document","created_at","survey_status"]


    