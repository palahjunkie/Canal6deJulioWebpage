# Generated by Django 4.1.3 on 2022-12-08 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_alter_project_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='director',
            field=models.TextField(blank=True, null=True),
        ),
    ]
