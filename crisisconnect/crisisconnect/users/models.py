from django.contrib.auth.models import AbstractUser
from django.db.models import *
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.utils import timezone


class User(AbstractUser):
    """
    Default custom user model for crisisconnect.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = CharField(_("Name of User"), blank=True, max_length=255)
    first_name = None  # type: ignore[assignment]
    last_name = None  # type: ignore[assignment]

    class GenderChoice(TextChoices):
        MALE = "M", _("Male")
        FEMALE = "F", _("Female")
        NOT_SPECIFIED = "N", _("Not Specified")

    gender = CharField(
        max_length=1, choices=GenderChoice.choices, default=GenderChoice.NOT_SPECIFIED
    )
    phone_number = PhoneNumberField(blank=True, unique=True, null=True)
    address = CharField(max_length=1000, blank=True, null=True)
    pincode = IntegerField(blank=True, null=True)

    class UserType(TextChoices):
        VICTIMS = "V", _("Victims")
        WARD_MEMBER = "W", _("Ward Member")
        COLLECTOR = "C", _("Collector")

    position = CharField(
        max_length=1,
        choices=UserType.choices,
        default=UserType.VICTIMS,
    )
    govt_id = CharField(max_length=100, blank=True, null=True,unique=True)
    is_completed=BooleanField(default=False)
    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})
