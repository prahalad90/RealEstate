# Generated by Django 4.2.5 on 2023-12-16 08:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('website', '0002_property_image1_property_image2_property_image3_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('image', models.FileField(blank=True, upload_to='./blog/')),
                ('altTag', models.CharField(blank=True, max_length=100)),
                ('content', models.TextField()),
                ('date', models.DateField()),
                ('slug', models.SlugField()),
                ('banner', models.ImageField(upload_to='./blog/')),
                ('altTag1', models.CharField(max_length=100)),
                ('page_title', models.CharField(max_length=200)),
                ('meta', models.CharField(max_length=400)),
                ('STATUS', models.CharField(choices=[('1', 'Draft'), ('2', 'Published')], default=1, max_length=2)),
                ('index', models.CharField(choices=[('index', 'index'), ('noindex', 'noindex')], default='index', max_length=8)),
                ('follow', models.CharField(choices=[('follow', 'follow'), ('nofollow', 'nofollow')], default='follow', max_length=8)),
                ('author', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]