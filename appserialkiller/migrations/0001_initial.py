# Generated by Django 4.1.2 on 2023-01-07 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Killer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=20)),
                ('apellido', models.CharField(max_length=30)),
                ('instagram', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='img', verbose_name='foto_usuario')),
            ],
        ),
    ]
