# Generated by Django 2.1.5 on 2019-10-29 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20191023_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='img',
            field=models.ImageField(null=True, upload_to='img/', verbose_name='缩略图'),
        ),
    ]
