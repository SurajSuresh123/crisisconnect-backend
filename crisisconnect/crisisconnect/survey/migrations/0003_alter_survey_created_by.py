# Generated by Django 4.2.11 on 2024-04-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("survey", "0002_rename_request_survey_request_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="survey",
            name="created_by",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]