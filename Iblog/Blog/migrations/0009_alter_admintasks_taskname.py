# Generated by Django 4.0.3 on 2022-06-23 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0008_admintasks_delete_adminemailcontroller'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admintasks',
            name='taskName',
            field=models.CharField(max_length=500),
        ),
    ]
