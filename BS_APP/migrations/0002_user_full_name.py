# Generated by Django 3.1.6 on 2021-02-04 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BS_APP', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='full_name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
