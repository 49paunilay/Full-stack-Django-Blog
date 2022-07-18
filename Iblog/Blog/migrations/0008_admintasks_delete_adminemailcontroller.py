# Generated by Django 4.0.3 on 2022-06-23 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog', '0007_adminemailcontroller_alter_category_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminTasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskName', models.EmailField(max_length=254)),
                ('description', models.TextField(default='Admin E-Mail Address')),
            ],
            options={
                'verbose_name_plural': ' Admin Tasks',
            },
        ),
        migrations.DeleteModel(
            name='AdminEmailController',
        ),
    ]