# Generated by Django 3.1.1 on 2020-09-29 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_length',
            field=models.CharField(default='', max_length=20),
            preserve_default=False,
        ),
    ]