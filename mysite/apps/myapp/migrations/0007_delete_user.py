# Generated by Django 4.0.4 on 2022-05-06 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_remove_user_gender_alter_user_mobile_num'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
