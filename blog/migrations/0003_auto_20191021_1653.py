# Generated by Django 2.1.5 on 2019-10-21 08:53

import DjangoUeditor.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20191021_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='body',
            field=DjangoUeditor.models.UEditorField(blank=True, verbose_name='内容'),
        ),
    ]
