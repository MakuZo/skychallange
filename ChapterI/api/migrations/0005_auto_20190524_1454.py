# Generated by Django 2.2.1 on 2019-05-24 12:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0004_auto_20190524_1447")]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="exam",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="tasks",
                to="api.Exam",
            ),
        )
    ]
