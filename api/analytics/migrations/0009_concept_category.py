# Generated by Django 2.1.3 on 2018-12-01 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0008_auto_20181201_1341'),
    ]

    operations = [
        migrations.AddField(
            model_name='concept',
            name='category',
            field=models.IntegerField(choices=[(0, 'Engels'), (1, 'Nederlands'), (2, 'Wiskunde'), (3, 'Aardrijkskunde'), (4, 'Geschiedenis')], default=2),
            preserve_default=False,
        ),
    ]
