# Generated by Django 4.1.3 on 2022-12-01 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0015_alter_emprestimos_data_devolucao_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='data_devolucao',
            field=models.DateField(blank=True, null=True, verbose_name='Data Devolução'),
        ),
        migrations.AlterField(
            model_name='emprestimos',
            name='data_emprestimo',
            field=models.DateField(blank=True, null=True),
        ),
    ]
