# Generated by Django 2.2.3 on 2022-03-30 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wallet', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appliedpromotion',
            name='promotion_rule',
        ),
    ]