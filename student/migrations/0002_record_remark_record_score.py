# Generated by Django 5.0.2 on 2024-02-19 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='record',
            name='remark',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='record',
            name='score',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=5),
        ),
    ]
