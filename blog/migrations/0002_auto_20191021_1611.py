# Generated by Django 2.1.5 on 2019-10-21 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='link',
            options={'verbose_name': '链接名称', 'verbose_name_plural': '链接名称'},
        ),
        migrations.AlterField(
            model_name='link',
            name='name',
            field=models.CharField(max_length=20, verbose_name='链接名称'),
        ),
    ]
