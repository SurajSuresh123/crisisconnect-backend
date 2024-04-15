from django.db import models
from django.contrib.auth import get_user_model
from crisisconnect.user_requests.models import UserRequest

User = get_user_model()
# Create your models here.
class Survey(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  request_id=models.ForeignKey(UserRequest,on_delete=models.CASCADE)
  survey_desc=models.CharField(max_length=1000)
  survey_doc=models.FileField(upload_to="survey_docs/",null=True,blank=True)
  created_at=models.DateTimeField(auto_now_add=True)
  created_by=models.CharField(max_length=100,blank=True,null=True)

  def __str__(self):
    return f"{self.user.username} {self.created_by}"