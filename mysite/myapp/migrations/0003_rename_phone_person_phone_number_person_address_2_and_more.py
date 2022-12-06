# Generated by Django 4.1.3 on 2022-12-06 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_alter_person_created_at_alter_person_gender_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='person',
            old_name='phone',
            new_name='phone_number',
        ),
        migrations.AddField(
            model_name='person',
            name='address_2',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='person',
            name='reference',
            field=models.CharField(default='', max_length=200),
        ),
    ]