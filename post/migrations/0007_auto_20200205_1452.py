# Generated by Django 3.0.3 on 2020-02-05 17:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0006_post_data'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Postagem', 'verbose_name_plural': 'Postagens'},
        ),
    ]
