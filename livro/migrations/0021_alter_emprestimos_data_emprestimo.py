# Generated by Django 4.1.1 on 2022-12-26 20:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0020_alter_emprestimos_avaliacao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 26, 17, 57, 6, 457031)),
        ),
    ]