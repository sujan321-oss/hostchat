# Generated by Django 4.1.2 on 2022-12-12 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("whatsapp", "0002_photos_user"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                    "photo",
                    models.FileField(default=None, null=True, upload_to="photos/"),
                ),
            ],
        ),
    ]