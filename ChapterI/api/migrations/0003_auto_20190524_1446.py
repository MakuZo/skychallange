# Generated by Django 2.2.1 on 2019-05-24 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("api", "0002_auto_20190524_1411")]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="grade",
            field=models.CharField(
                blank=True,
                choices=[(5, "A"), (4, "B"), (3, "C"), (2, "D"), (1, "F")],
                max_length=1,
                null=True,
            ),
        )
    ]
