# Generated by Django 2.2.1 on 2019-05-24 12:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0001_initial")]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="examinee",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="sheets",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="exam",
            name="examiner",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="exams",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
