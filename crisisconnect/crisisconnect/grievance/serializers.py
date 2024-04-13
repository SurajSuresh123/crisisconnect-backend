from rest_framework import serializers
from .models import Grievance


class CreateGrievanceSerializer(serializers.ModelSerializer):

    class Meta:
        model = Grievance
        fields = ["id", "grievance_desc", "request_id","created_at"]

class RetrieveGrievanceSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")

    def get_username(self,obj:Grievance):
        return obj.user.username
    
    class Meta:
        model = Grievance
        fields = ["id","username","request_id","grievance_desc","created_at"]

