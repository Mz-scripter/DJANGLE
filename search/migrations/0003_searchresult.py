# Generated by Django 5.1.4 on 2024-12-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_djangledb_search_vector_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SearchResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField(max_length=255)),
                ('content', models.TextField()),
                ('keywords', models.JSONField(blank=True, null=True)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
    ]
