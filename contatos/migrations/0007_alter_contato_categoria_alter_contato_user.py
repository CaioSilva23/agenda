# Generated by Django 4.1.7 on 2023-03-09 12:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contatos', '0006_alter_contato_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contato',
            name='categoria',
            field=models.ForeignKey(default='Sem categoria', on_delete=django.db.models.deletion.SET_DEFAULT, to='contatos.categoria'),
        ),
        migrations.AlterField(
            model_name='contato',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
