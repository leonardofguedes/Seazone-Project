# Generated by Django 3.1.5 on 2023-01-08 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Imovel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_imovel', models.CharField(max_length=200)),
                ('limite_hospedes', models.IntegerField()),
                ('quantidade_banheiros', models.IntegerField()),
                ('aceita_animais', models.BooleanField(default=False)),
                ('valor_limpeza', models.DecimalField(decimal_places=2, max_digits=8)),
                ('data_ativacao', models.DateField()),
                ('criado_em', models.DateTimeField(auto_now_add=True)),
                ('atualizado_em', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
