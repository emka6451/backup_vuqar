# Generated by Django 3.2.11 on 2022-03-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_delete_mobil_haqqımızdafoto'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobileHaqqımızda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foto', models.ImageField(upload_to='media/')),
            ],
        ),
    ]
