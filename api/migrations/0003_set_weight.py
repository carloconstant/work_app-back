# Generated by Django 3.0 on 2021-04-15 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20210414_1045'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='weight',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
