# Generated by Django 3.2.4 on 2021-06-11 13:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ('name',), 'verbose_name': 'category', 'verbose_name_plural': 'categories'},
        ),
    ]
