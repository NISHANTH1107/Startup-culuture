# Generated by Django 5.1.4 on 2025-04-05 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('career_site', '0004_alter_careerlibrary_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='careerlibrary',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='career_library/'),
        ),
    ]
