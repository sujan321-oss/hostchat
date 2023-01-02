# Generated by Django 4.1.2 on 2022-12-13 21:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("whatsapp", "0004_usergroup_chat"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usergroup", old_name="groupname", new_name="usergroupname",
        ),
        migrations.AlterField(
            model_name="chat",
            name="groupname",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="whatsapp.usergroup",
                unique=True,
            ),
        ),
    ]