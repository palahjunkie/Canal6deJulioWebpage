# Generated by Django 4.1.3 on 2022-12-08 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_year'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
