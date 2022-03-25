# Generated by Django 3.2.11 on 2022-01-27 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Xidmətlər',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.ImageField(upload_to='media/')),
                ('basliq', models.TextField(max_length=50000)),
                ('kicik_metn', models.TextField(max_length=50000)),
                ('vaxt', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Xidmətlər_ÜstMətn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('basliq', models.TextField(max_length=50000)),
                ('metn', models.TextField(max_length=50000)),
            ],
        ),
    ]
