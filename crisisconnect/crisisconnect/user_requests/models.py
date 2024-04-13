from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

User = get_user_model()
# Create your models here.


class UserRequest(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class RequestType(models.TextChoices):
        BASIC_ITEMS = "B", _("Basic items")
        MEDICINES = "M", _("Medicines")

    type = models.CharField(
        max_length=1,
        choices=RequestType.choices,
        default=RequestType.BASIC_ITEMS,
    )
    request_desc = models.CharField(max_length=1000)
    document = models.FileField(
        upload_to="user_requests/upload_docs", null=True, blank=True
    )
    medical_document = models.FileField(
        upload_to="user_requests/med_docs", null=True, blank=True
    )
    approved = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "-" + self.type
