# Generated by Django 4.1.7 on 2023-03-09 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0008_alter_contato_categoria'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contato',
            name='categoria',
        ),
    ]
