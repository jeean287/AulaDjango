# Generated by Django 3.0.3 on 2020-02-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0004_auto_20200205_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='conteudo',
            field=models.TextField(default='', max_length=280, verbose_name='contDDDSeudo'),
        ),
    ]
