# Generated by Django 3.1.1 on 2021-02-03 09:59

import contact_page.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact_page', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='meeting',
            name='token',
            field=models.CharField(default='0000000000000000000000000000000000000000000000000000000000000000', max_length=64, validators=[contact_page.models.hashvalidator]),
        ),
    ]
