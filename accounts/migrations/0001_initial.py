# Generated by Django 3.2.7 on 2021-10-11 20:04

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('name', models.CharField(max_length=200)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('quantity', models.IntegerField()),
                ('is_published', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(blank=True, default=datetime.datetime.now)),
                ('category', models.ForeignKey(default=False, null=True, on_delete=django.db.models.deletion.CASCADE, to='accounts.category')),
            ],
        ),
    ]
