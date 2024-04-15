from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.
class feedback(models.Model):
  user=models.ForeignKey(User,on_delete=models.CASCADE)
  feedback_desc=models.CharField(max_length=1000)
  proof_docs= models.FileField(
        upload_to="feedback/proof_docs", null=True, blank=True
    )
  created_at = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.user.username} Feedback no -{str(self.id)}"