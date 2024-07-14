# Generated by Django 4.2.3 on 2024-07-13 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('published_date', models.DateField()),
                ('isbn', models.CharField(max_length=13)),
                ('pages', models.IntegerField()),
                ('language', models.CharField(max_length=50)),
                ('publisher', models.CharField(max_length=100)),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='covers/')),
            ],
        ),
    ]
