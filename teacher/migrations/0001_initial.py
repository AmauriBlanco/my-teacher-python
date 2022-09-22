# Generated by Django 4.1.1 on 2022-09-21 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('valor_hora', models.DecimalField(decimal_places=2, max_digits=9)),
                ('descricao', models.TextField()),
                ('foto', models.URLField(max_length=255)),
            ],
        ),
    ]
