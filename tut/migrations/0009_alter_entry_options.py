# Generated by Django 4.0.3 on 2022-06-26 13:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tut', '0008_author_blog_myperson_entry'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'Entries'},
        ),
    ]
