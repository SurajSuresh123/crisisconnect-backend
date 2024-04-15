from rest_framework import serializers
from .models import feedback


class CreateFeedbackSerializer(serializers.ModelSerializer):

    class Meta:
        model = feedback
        fields = ["id", "feedback_desc", "created_at"]

class RetrieveFeedbackSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField("get_username")

    def get_username(self,obj:feedback):
        return obj.user.username
    
    class Meta:
        model = feedback
        fields = ["id","username", "feedback_desc", "created_at"]
