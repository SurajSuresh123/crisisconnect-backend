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
    aadhar_no=models.CharField(max_length=12,blank=True)
    ration_no=models.CharField(max_length=10,blank=True)
    class ApprovedType(models.TextChoices):
        PENDING = "P", _("Pending")
        APPROVED = "A", _("Approved")
        REJECTED = "R", _("Rejected")

    survey_status = models.CharField(
        max_length=1,
        choices=ApprovedType.choices,
        default=ApprovedType.PENDING,
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username + "-" + self.type
