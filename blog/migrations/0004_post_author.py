# Generated by Django 5.1.4 on 2024-12-13 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remove_post_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='author',
            field=models.CharField(default=1, max_length=30),
            preserve_default=False,
        ),
    ]
