from rest_framework import serializers

from crisisconnect.users.models import User


class UserSerializer(serializers.ModelSerializer[User]):
    class Meta:
        model = User
        fields = ["username", "name", "gender","email","phone_number","address","pincode","position","govt_id","is_completed"]

        # extra_kwargs = {
        #     "url": {"view_name": "api:user-detail", "lookup_field": "username"},
        # }
