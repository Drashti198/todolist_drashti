# Generated by Django 4.2.3 on 2023-07-05 04:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base", "0002_task_inprogress"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="task", options={"ordering": ["complete", "inprogress"]},
        ),
    ]
