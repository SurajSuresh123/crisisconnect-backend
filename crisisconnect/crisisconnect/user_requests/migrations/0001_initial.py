# Generated by Django 4.2.11 on 2024-03-30 08:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="UserRequest",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[("B", "Basic items"), ("M", "Medicines")],
                        default="B",
                        max_length=1,
                    ),
                ),
                ("request_desc", models.CharField(max_length=1000)),
                (
                    "document",
                    models.FileField(
                        blank=True, null=True, upload_to="user_requests/upload_docs"
                    ),
                ),
                (
                    "medical_document",
                    models.FileField(
                        blank=True, null=True, upload_to="user_requests/med_docs"
                    ),
                ),
                ("approved", models.BooleanField(default=False)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
