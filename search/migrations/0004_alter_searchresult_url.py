# Generated by Django 5.1.4 on 2024-12-18 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0003_searchresult'),
    ]

    operations = [
        migrations.AlterField(
            model_name='searchresult',
            name='url',
            field=models.URLField(unique=True),
        ),
    ]
