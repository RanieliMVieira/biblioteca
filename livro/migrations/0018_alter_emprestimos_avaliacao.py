# Generated by Django 4.1.3 on 2022-12-02 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('livro', '0017_emprestimos_avaliacao'),
    ]

    operations = [
        migrations.AlterField(
            model_name='emprestimos',
            name='avaliacao',
            field=models.CharField(blank=True, choices=[('P', 'Péssimo'), ('R', 'Ruim'), ('B', 'Bom'), ('O', 'Ótimo')], max_length=1),
        ),
    ]