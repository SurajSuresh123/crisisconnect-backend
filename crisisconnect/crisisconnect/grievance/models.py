from django.db import models
from django.contrib.auth import get_user_model
from crisisconnect.user_requests.models import UserRequest
from crisisconnect.survey.models import Survey

# Create your models here.
User = get_user_model()


class Grievance(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_id = models.ForeignKey(UserRequest, on_delete=models.CASCADE)
    grievance_desc = models.CharField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + " Grievance no -" + str(self.id)
