# Generated by Django 2.1.3 on 2018-11-27 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('assinaki', '0022_assinatura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dados_cartao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cartao_nome', models.CharField(max_length=150, verbose_name='Cartão')),
                ('cartao_numero', models.CharField(max_length=50, verbose_name='Número')),
                ('cartao_data', models.DateField(verbose_name='Data')),
                ('cartao_security_cod', models.CharField(max_length=10, verbose_name='Código')),
                ('cartao_password', models.CharField(max_length=150, verbose_name='Password')),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='assinaki.Pais')),
            ],
            options={
                'verbose_name': 'Dados_cartao',
                'verbose_name_plural': 'Dados_cartao',
            },
        ),
    ]
