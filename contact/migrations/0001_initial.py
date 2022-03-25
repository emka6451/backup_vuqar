# Generated by Django 3.2.11 on 2022-01-27 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Form_Şəkil',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='media/')),
            ],
        ),
        migrations.CreateModel(
            name='Telefon_Email_Mekan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('telefon', models.IntegerField()),
                ('email', models.CharField(max_length=50000)),
                ('mekan', models.TextField(max_length=50000)),
            ],
        ),
    ]