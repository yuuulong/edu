# Generated by Django 2.0 on 2019-01-05 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0013_auto_20190103_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='points',
            field=models.CharField(max_length=120, verbose_name='教学特点'),
        ),
    ]