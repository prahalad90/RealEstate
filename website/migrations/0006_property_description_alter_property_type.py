# Generated by Django 4.2.5 on 2023-12-25 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_property_bed'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='description',
            field=models.CharField(default='Text', max_length=1000),
        ),
        migrations.AlterField(
            model_name='property',
            name='type',
            field=models.CharField(choices=[('Residential', 'Residential'), ('2', 'Commercial')], default='1', max_length=12),
        ),
    ]
