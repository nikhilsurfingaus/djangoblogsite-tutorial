# Generated by Django 4.1.5 on 2023-01-25 01:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_blogpost_publish_date_blogpost_timestamp_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-publish_date', '-updated', '-timestamp']},
        ),
    ]