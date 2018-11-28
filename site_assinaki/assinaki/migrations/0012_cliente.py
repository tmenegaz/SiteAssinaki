# Generated by Django 2.1.3 on 2018-11-27 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assinaki', '0011_auto_20181127_1324'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente_nome', models.CharField(max_length=150, verbose_name='Nome')),
                ('rua', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assinaki.Rua')),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
    ]
