# Generated by Django 2.0 on 2018-12-29 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0005_teacher_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='courseorg',
            name='tag',
            field=models.CharField(default='', max_length=10, verbose_name='课程标签'),
        ),
    ]
