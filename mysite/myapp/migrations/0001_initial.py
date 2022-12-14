# Generated by Django 4.1.3 on 2022-12-05 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=50)),
                ('gender', models.BooleanField()),
                ('created_at', models.DateTimeField()),
                ('updated_at', models.DateTimeField()),
            ],
        ),
    ]
