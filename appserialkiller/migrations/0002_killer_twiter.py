# Generated by Django 4.1.2 on 2023-01-31 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appserialkiller', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='killer',
            name='twiter',
            field=models.CharField(default='martinflow', max_length=30),
            preserve_default=False,
        ),
    ]