# Generated by Django 4.1.3 on 2022-12-09 23:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0012_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, default='unam.jpg', null=True, upload_to=''),
        ),
    ]