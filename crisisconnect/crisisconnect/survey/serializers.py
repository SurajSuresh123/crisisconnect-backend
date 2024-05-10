from rest_framework import serializers
from .models import Survey

class CreateSurveySerializer(serializers.ModelSerializer):
    approved=serializers.SerializerMethodField("get_approved")
    def get_approved(self,obj:Survey):
        return obj.request_id.approved
    class Meta:
      model=Survey
      fields=["id","request_id","survey_desc","survey_doc","created_at","created_by","approved"]


class RetrieveSurveySerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")

    def get_username(self,obj:Survey):
        return obj.user.username
    
    class Meta:
        model = Survey
        fields = ["id","username","survey_desc", "survey_doc","created_at","created_by"]