# Generated by Django 2.1.3 on 2018-11-27 16:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assinaki', '0010_cliente'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cliente',
            name='rua',
        ),
        migrations.DeleteModel(
            name='Cliente',
        ),
    ]
