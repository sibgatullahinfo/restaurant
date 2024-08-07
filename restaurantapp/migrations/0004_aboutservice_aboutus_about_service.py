# Generated by Django 5.0.6 on 2024-05-16 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurantapp', '0003_aboutitem_aboutus'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('service_title', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='aboutus',
            name='about_service',
            field=models.ManyToManyField(to='restaurantapp.aboutservice'),
        ),
    ]
