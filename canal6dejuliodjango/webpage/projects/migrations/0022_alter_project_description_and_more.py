# Generated by Django 4.1.3 on 2022-12-13 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0021_alter_project_featured_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(blank=True, default='unam.png', null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
