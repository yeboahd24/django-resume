# Generated by Django 3.1.13 on 2021-07-30 10:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=25)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=200)),
                ('zipcode', models.CharField(max_length=5)),
                ('person', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='people.person')),
            ],
        ),
    ]
